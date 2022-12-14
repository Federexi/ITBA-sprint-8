from ast import If
from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Clientes.models import Cliente, Empleado
from .forms import UserRegistrationForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.


def index1 (request):
    return render (request, 'Login/templates/registration/login.html')


class signup(generic.CreateView):
    template_name = 'registration/registro.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('hub')
   

    # def form_valid(self, form):
    #     try:
    #         cliente = Cliente.objects.get(customer_dni=form.cleaned_data.get('dni'))
    #     except Cliente.DoesNotExist:
    #         cliente = None
    #     if not cliente:
    #         form.add_error('dni', 'El cliente no existe')
    #         return self.form_invalid(form)
    #     elif cliente.user_id:
    #         form.add_error('dni', error='El cliente ya tiene un usuario para operar en Home Banking')
    #         return self.form_invalid(form)
            
    #     super(signup, self).form_valid(form) 
    #     new_user = self.object 
    #     cliente.user_id = new_user
    #     cliente.save()
    #     username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
    #     new_user = authenticate(username=username, password=password)
    #     login(self.request, new_user)
    #     return HttpResponseRedirect(reverse('hub'))   

    
    def form_valid(self, form):
        categoria = form.cleaned_data.get('last_name').lower()
        if categoria == 'empleado':
            try:
                empleado = Empleado.objects.get(employee_dni=form.cleaned_data.get('dni'))
            except Empleado.DoesNotExist:
                empleado = None
            if not empleado:
                form.add_error('dni', 'El empleado no existe')
                return self.form_invalid(form)
            elif empleado.user_id:
                form.add_error('dni', error='El empleado ya tiene un usuario para operar en Home Banking')
                return self.form_invalid(form)
                
            super(signup, self).form_valid(form) 
            new_user = self.object 
            new_user.is_staff = True
            new_user.save()
            empleado.user_id = new_user
            empleado.save()
            username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
            new_user = authenticate(username=username, password=password)
            login(self.request, new_user)
            return HttpResponseRedirect(reverse('hub'))  

        elif categoria == 'cliente':
            try:
                cliente = Cliente.objects.get(customer_dni=form.cleaned_data.get('dni'))
            except Cliente.DoesNotExist:
                cliente = None
            if not cliente:
                form.add_error('dni', 'El cliente no existe')
                return self.form_invalid(form)
            elif cliente.user_id:
                form.add_error('dni', error='El cliente ya tiene un usuario para operar en Home Banking')
                return self.form_invalid(form)
                
            super(signup, self).form_valid(form) 
            new_user = self.object 
            cliente.user_id = new_user
            cliente.save()
            username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
            new_user = authenticate(username=username, password=password)
            login(self.request, new_user)
            return HttpResponseRedirect(reverse('hub'))  

        else:
            form.add_error('last_name', 'La categor??a ingresada es inv??lida')
            return self.form_invalid(form)