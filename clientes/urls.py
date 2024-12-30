from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='inicio'),
    path('prueba/', views.prueba, name='prueba'),
    path('', views.listar_clientes, name='listar_clientes'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('<int:cliente_id>/modificar/', views.modificar_cliente, name='modificar_cliente'),
    path('<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('<int:cliente_id>/', views.visualizar_cliente, name='visualizar_cliente'),
]