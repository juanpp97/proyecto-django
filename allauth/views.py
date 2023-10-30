from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from allauth.forms import  InicioSesionForm, RegistroForm



class Handler_Login_Registration(TemplateView):
    template_name = 'accounts/combined_registration_login.html'
    
    def get(self, request):
        login_form = InicioSesionForm()
        registration_form = RegistroForm()
        return render(request, self.template_name, {'registration_form': registration_form, 'login_form': login_form, "LoginOrRegister": False })

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
                    return redirect('index')
                else:
                    login_form.add_error(None,'Credenciales incorrectas!.')
                    pass
            else:
                pass
        else:
            login_form = InicioSesionForm()
        if 'registration_form' in request.POST:
            registration_form = RegistroForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                return redirect('index')
            else:
                panel = True

                pass

        else:
            registration_form = RegistroForm()
        
        return render(request,'accounts/combined_registration_login.html', {'registration_form': registration_form, 'login_form': login_form,"LoginOrRegister": panel })


