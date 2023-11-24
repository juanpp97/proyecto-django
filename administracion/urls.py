from django.urls import path
from . import views

urlpatterns = [
    path('tipo_habitaciones/', views.RoomTypeListView.as_view(), name = 'listar_tipo_hab'),
    path('tipo_habitaciones/crear', views.RoomTypeCreateView.as_view(), name = 'crear_tipo_hab'),
    path('tipo_habitaciones/editar/<int:pk>', views.RoomTypeUpdateView.as_view(), name = 'editar_tipo_hab'),
    path('tipo_habitaciones/eliminar/<int:pk>', views.RoomTypeDeleteView.as_view(), name = 'eliminar_tipo_hab'),
    path('vista/', views.RoomViewListView.as_view(), name = 'listar_vista'),
    path('vista/crear', views.RoomViewCreateView.as_view(), name = 'crear_vista'),
    path('vista/editar/<int:pk>', views.RoomViewUpdateView.as_view(), name = 'editar_vista'),
    path('vista/eliminar/<int:pk>', views.RoomViewDeleteView.as_view(), name = 'eliminar_vista'),
    path('tarifa/', views.PriceListView.as_view(), name = 'listar_tarifa'),
    path('tarifa/crear', views.PriceCreateView.as_view(), name = 'crear_tarifa'),
    path('tarifa/editar/<int:pk>', views.PriceUpdateView.as_view(), name = 'editar_tarifa'),
    path('tarifa/eliminar/<int:pk>', views.PriceDeleteView.as_view(), name = 'eliminar_tarifa'),
    path('habitaciones/', views.RoomListView.as_view(), name = 'listar_hab'),
    path('habitaciones/crear', views.RoomCreateView.as_view(), name = 'crear_hab'),
    path('habitaciones/editar/<int:pk>', views.RoomUpdateView.as_view(), name = 'editar_hab'),
    path('habitaciones/eliminar/<int:pk>', views.RoomDeleteView.as_view(), name = 'eliminar_hab'),
    
    
] 