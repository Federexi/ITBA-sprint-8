from django.shortcuts import render
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from .models import Tarjeta
""" from .serializers import TarjetaSerializer
from rest_framework import viewsets
from Clientes.models import Empleado """


def index3 (request):
    try:
        datacliente = Cliente.objects.get(user_id = request.user.id)
        try:
            datacuenta = Cuenta.objects.filter(customer_id = datacliente.customer_id)
            largodatacuenta = len(Cuenta.objects.filter(customer_id = datacliente.customer_id))
        except:
            datacuenta = None
        
        if largodatacuenta == 0: 
                datatarjeta = None
        else:
            datatarjeta = []
            for c in datacuenta:
                x = Tarjeta.objects.filter(account_id = c.account_id)
                if x:
                    datatarjeta.append(x)

        return render (request, 'Tarjetas/template/Tarjetas/gestiones.html', context={'datacliente':datacliente, 'datacuenta':datacuenta, 'datatarjeta':datatarjeta})

    except:
        return render (request, 'Tarjetas/template/Tarjetas/gestiones.html', context={'datacliente':None, 'datacuenta':None, 'datatarjeta':None})



""" class TarjetasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TarjetaSerializer
    def get_queryset(self):
        id = self.request.user.id
        empleado = Empleado.objects.filter(user_id = id)
        tarjeta_id = empleado[0].branch_id
        lista_clientes = Cliente.objects.filter(branch_id = tarjeta_id)
        lista = []
        tarjetas = Tarjeta.objects.all()
        for p in tarjetas:
            for c in lista_clientes:
                if p.customer_id == c.customer_id:
                    lista.append(p) 
        return lista """
