from http import client
from django.shortcuts import render
from Clientes.models import Cliente, Direccion
from Cuentas.models import Cuenta
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views import generic
from Clientes.serializers import DireccionesSerializer, MiDireccionSerializer
from .forms import LoanForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.db import connection
from .models import Prestamo, Sucursal
from Clientes.models import Empleado
from .serializers import SucursalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, status


@method_decorator(login_required, name='dispatch')
class LoanRequest(generic.CreateView):
    form_class = LoanForm
    success_url = reverse_lazy('prestamos')
    template_name = 'Prestamos/template/Prestamos/prestamos.html'

    def form_valid(self, form):
        try:
            user = self.request.user
            cliente = Cliente.objects.get(user_id = user.id)
            hoy = datetime.date(datetime.now())
            currenttime = datetime.now()
            hora = currenttime.strftime('%H:%M:%S')
            diaenform = form.cleaned_data.get('loan_date')
            datacuenta = Cuenta.objects.filter(customer_id = cliente.customer_id)
            cuentapesos = None
            cuentacorri = None
            
            for c in datacuenta:
                if c.type == 'Caja de ahorro en pesos':
                    cuentapesos = c.account_id

            if not cuentapesos:
                for c in datacuenta:
                    if c.type == 'Cuenta Corriente':
                        cuentacorri = c.account_id
                        break
            
            if cuentapesos:
                numerocuenta = cuentapesos
            else:
                numerocuenta = cuentacorri

            montoenform = form.cleaned_data.get('loan_total')
            montoactualizado = montoenform * 100

            def balanceupdate(self,montoactualizado,numerocuenta):
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE cuenta SET balance = balance + %s WHERE account_id = %s", [montoactualizado, numerocuenta])

            def movimupdate(self,numerocuenta,montoenform,hora):
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO movimientos(no_account, amount, type_operation, hour) VALUES(%s, %s, 'Préstamo', %s)", [numerocuenta,montoenform,hora])

            if not datacuenta:
                form.add_error(field = None, error = 'El cliente no posee una cuenta')
                return self.form_invalid(form)

            if not cliente.approve_loan(form.cleaned_data.get('loan_total')):
                form.add_error(field = None, error = 'Préstamo rechazado')
                return self.form_invalid(form)
            
            if not diaenform >= hoy:
                form.add_error(field = None, error = 'La fecha solicitada es inválida')
                return self.form_invalid(form)

            else:
                balanceupdate(self,montoactualizado,numerocuenta)
                movimupdate(self,numerocuenta,montoenform,hora)
                form.instance.customer_id = cliente.customer_id
                super(LoanRequest, self).form_valid(form)

            return render(self.request, 'Prestamos/template/Prestamos/prestamos.html', context={'form': form, 'success_msg': 'Préstamo aprobado', 'cuentapesos':cuentapesos, 'cuentacorri':cuentacorri})

        except:
            form.add_error(field = None, error = 'Un empleado no puede solicitar un préstamo')
            return self.form_invalid(form)


class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SucursalSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        lista_clientes = Cliente.objects.filter(branch_id = id)
        lista = []
        prestamos = Prestamo.objects.all()
        for p in prestamos:
            for c in lista_clientes:
                if p.customer_id == c.customer_id:
                    lista.append(p) 
        return lista 

class SolicitudPrestamoViewSet(viewsets.ModelViewSet): 
    permission_classes = [IsAdminUser]
    serializer_class = SucursalSerializer
    queryset = Prestamo.objects.all()
    lookup_field = 'loan_id'

    def get(self, request, format=None):
        prestamos = Prestamo.objects.all()
        serializer = SucursalSerializer(prestamos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModificarDireccionesViewSet(viewsets.mixins.ListModelMixin,viewsets.mixins.RetrieveModelMixin, viewsets.mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = DireccionesSerializer
    queryset = Direccion.objects.all()


class ModificarMiDireccionViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = MiDireccionSerializer
    
    def get_queryset(self):
        id = self.request.user.id
        cliente = Cliente.objects.filter(user_id = id) 
        try:
            cl_id = cliente[0].customer_id
            return Direccion.objects.filter(customer = cl_id)
        except:
            direcciones = []
            return direcciones
            