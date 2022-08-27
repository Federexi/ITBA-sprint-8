
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Clientes.models import Cliente
from .models import Cuenta
from .models import Movimientos
# from .serializers import CuentaSerializer
from rest_framework import viewsets

# class CuentaViewSet(viewsets.mixins.ListModelMixin,viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     serializer_class = CuentaSerializer
#     def get_queryset(self):
#         id = self.request.user.id
#         cliente = Cliente.objects.filter(user_id = id)
#         cl_id = cliente[0].customer_id
#         return Cuenta.objects.filter(customer_id = cl_id)

@login_required
def act (request):
    try:
        datacliente = Cliente.objects.get(user_id = request.user.id)
        try:
            datacuenta = Cuenta.objects.filter(customer_id = datacliente.customer_id)
            largodatacuenta = len(Cuenta.objects.filter(customer_id = datacliente.customer_id))
        except:
            datacuenta = None
        
        if largodatacuenta <= 1:
            try:
                datamovimientos = [Movimientos.objects.filter(no_account = datacuenta[0].account_id)]
            except:
                datamovimientos = None
        else:
            datamovimientos = []
            for c in datacuenta:
                x = Movimientos.objects.filter(no_account = c.account_id)
                datamovimientos.append(x)

        return render (request, 'Cuentas/template/Cuentas/actividad.html', context={'datacliente':datacliente, 'datacuenta':datacuenta, 'datamovimientos':datamovimientos, 'largodatacuenta': largodatacuenta })

    except:
        return render (request, 'Cuentas/template/Cuentas/actividad.html', context={'datacliente':None, 'datacuenta':None, 'datamovimientos':None, 'largodatacuenta': None })

@login_required
def conf (request):
    return render (request, 'Cuentas/template/Cuentas/configuracion.html')

@login_required
def hub (request):
    try:
        datacliente = Cliente.objects.get(user_id = request.user.id)
        try:
            datacuenta = Cuenta.objects.filter(customer_id = datacliente.customer_id)
        except:
            datacuenta = None
        return render (request, 'Cuentas/template/Cuentas/hub.html', context={'datacliente':datacliente, 'datacuenta':datacuenta })
    except:
        return render (request, 'Cuentas/template/Cuentas/hub.html', context={'datacliente':None, 'datacuenta':None })

@login_required
def inv (request):
    return render (request, 'Cuentas/template/Cuentas/inversiones.html')
    
@login_required
def seg (request):
    return render (request, 'Cuentas/template/Cuentas/seguridad.html')

@login_required
def transf (request):
    try:
        datacliente = Cliente.objects.get(user_id = request.user.id)
        try:
            datacuenta = Cuenta.objects.filter(customer_id = datacliente.customer_id)
        except:
            datacuenta = None
        return render (request, 'Cuentas/template/Cuentas/transferencias.html', context={'datacliente':datacliente, 'datacuenta':datacuenta})
    except:
        return render (request, 'Cuentas/template/Cuentas/transferencias.html', context={'datacliente':None, 'datacuenta':None})