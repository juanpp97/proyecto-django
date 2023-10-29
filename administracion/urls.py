from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.RoomListView.as_view(), name = 'listar_hab'),
    path('habitaciones/crear', views.RoomCreateView.as_view(), name = 'crear_hab'),
    path('habitaciones/editar/<int:pk>', views.RoomUpdateView.as_view(), name = 'editar_hab'),
    path('habitaciones/eliminar/<int:pk>', views.RoomDeleteView.as_view(), name = 'eliminar_hab'),
<<<<<<< HEAD
    path('vista/crear', views.RoomViewCreateView.as_view(), name = 'crear_vista'),
=======
    path('vista/', views.RoomViewListView.as_view(), name = 'listar_vista'),
    path('vista/crear', views.RoomViewCreateView.as_view(), name = 'crear_vista'),
    path('vista/editar/<int:pk>', views.RoomViewCreateView.as_view(), name = 'editar_vista'),
    path('vista/eliminar/<int:pk>', views.RoomViewCreateView.as_view(), name = 'eliminar_vista'),
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
    
    
] 