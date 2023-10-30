from django.contrib.auth import login,authenticate,get_user_model
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from allauth.forms import  InicioSesionForm, RegistroForm

User = get_user_model()


# class RegistroView(CreateView):
#     model = User
#     form_class = CustomUserCreationForm
#     template_name = 'accounts/registro.html'
#     success_url = reverse_lazy('index')  # Redirige a la página de inicio después del registro

#     def form_valid(self, form):
#         # Este método se llama cuando el formulario es válido, antes de guardar el usuario
#         # Aquí puedes realizar acciones adicionales si es necesario
#         response = super().form_valid(form)
#         login(self.request, self.object)  # Inicia sesión al usuario después del registro
#         return response

# class CustomLoginView(LoginView):
#     template_name = 'accounts/custom_login.html'
#     def get_success_url(self):
#         return reverse_lazy('index')

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         return response
    


# def verificar_usuario_registrado(username):
#     try:
#         # Intenta obtener un usuario por su nombre de usuario
#         usuario = User.objects.get(username=username)
#         return usuario  # Retorna el usuario si se encuentra en la base de datos
#     except User.DoesNotExist:
#         return None 


class Handler_Login_Registration(TemplateView):
    template_name = 'accounts/combined_registration_login.html'

    
    def get(self, request):
        login_form = InicioSesionForm()
        registration_form = RegistroForm()
        return render(request, self.template_name, {'registration_form': registration_form, 'login_form': login_form})

    def post(self, request):
        print(request.POST)
        if 'login_form' in request.POST:
            print("si es login")

            login_form = InicioSesionForm(request,data=request.POST)
         
            if login_form.clean():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                print(f"es valido {username} {password}")
   
                user = authenticate(request, username=username, password=password)
                if user is not None: 
                    print("si Existe")
                    login(request,user)
                    return redirect('index')
                else:
                    print("no Existe")
                    login_form.add_error(None,'Credenciales incorrectas!.')
            else:
                print("no es valido")
                pass
        else:
            print("no es login")
            login_form = InicioSesionForm()

        # if 'registrarion_form' in request.POST:
        #     print("si es registro")

        #     registration_form = InicioSesionForm(request.POST)
        #     if registration_form.is_valid():
        #         usuario = registration_form.save()
        #         login(request, usuario)  # Iniciar sesión después del registro
        #         return redirect('index')  # Redirigir a la página de perfil u otra página después del registro
        #     else:
        #          registration_form.add_error(None, "Credenciales incorrectas")
        # else:
        #     registration_form = RegistroForm()

        if 'registration_form' in request.POST:
            print("si es registro")

            registration_form = RegistroForm(request.POST)
           
        else:
            registration_form = RegistroForm()
        
        return render(request,'accounts/combined_registration_login.html', {'registration_form': registration_form, 'login_form': login_form})

    # return render(request, 'combined_registration_login.html', {'login_form': login_form, 'registration_form': registration_form})