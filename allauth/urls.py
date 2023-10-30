from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('home', views.CombinedRegistrationLoginView.as_view(), name='combined_registration_login'),
    # path('register/', views.RegistroView.as_view(), name='register'),
    path('', views.Handler_Login_Registration.as_view(), name='accounts-hanfler'),

   # path('login/', views.LoginView.as_view(), name='login')
    ] 

