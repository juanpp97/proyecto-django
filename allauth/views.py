from typing import Any
from django import http
from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from allauth.forms import  InicioSesionForm, RegistroForm
from django.contrib import messages



class Handler_Login_Registration(TemplateView):
    template_name = 'accounts/combined_registration_login.html'
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect(reverse_lazy('index'))
    #     return super().dispatch(request, *args, **kwargs)
    def get(self, request):

        panel = False
        if request.GET.get('panel') == 'True':
            panel = True
            print(request.GET.get('panel'))
        login_form = InicioSesionForm()
        registration_form = RegistroForm()
        return render(request, self.template_name, {'registration_form': registration_form, 'login_form': login_form, "LoginOrRegister": panel })

    def post(self, request):
        panel=False
        if 'login_form' in request.POST:
            login_form = InicioSesionForm(request,data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None: 
                    login(request,user)
                    if 'next' in request.POST:
                        return redirect(request.POST['next'])
                    return redirect('index')
                else:
                    login_form.add_error(None,'Credenciales incorrectas!.')
                    pass
            else:
                messages.error(request, "Error al iniciar sesión")

        else:
            login_form = InicioSesionForm()
        if 'registration_form' in request.POST:
            registration_form = RegistroForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                panel = False
                messages.success(request, "Usuario creado correctamente")
                return redirect('accounts-hanfler')
            else:
                panel = True
                messages.error(request, "Se ha producido un error al crear el usuario")
                pass

        else:
            registration_form = RegistroForm()
        
        return render(request,'accounts/combined_registration_login.html', {'registration_form': registration_form, 'login_form': login_form,"LoginOrRegister": panel })


