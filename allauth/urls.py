from django.urls import include, path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('home', views.CombinedRegistrationLoginView.as_view(), name='combined_registration_login'),
    # path('register/', views.RegistroView.as_view(), name='register'),
    path('', views.Handler_Login_Registration.as_view(), name='accounts_handler'),
    path('logout/', LogoutView.as_view(), name="logout")
   # path('login/', views.LoginView.as_view(), name='login')
    ] 

