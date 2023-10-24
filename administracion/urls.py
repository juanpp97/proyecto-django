from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.RoomListView.as_view(), name = 'listar_hab'),
    path('habitaciones/crear', views.RoomCreateView.as_view(), name = 'crear_hab'),
    path('vista/crear', views.RoomViewCreateView.as_view(), name = 'crear_vista'),
    
    
]