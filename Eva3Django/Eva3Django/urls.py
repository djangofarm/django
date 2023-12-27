from django.contrib import admin
from django.urls import path
from tienda import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),
    path('productos', views.productos, name='productos'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('sucursales', views.sucursales, name='sucursales'),
    path('contacto', views.contacto, name='contacto'),
    path('gracias', views.gracias, name='gracias'),
    path('crear', views.crearProducto, name='crearProducto'),
    path('editar', views.editarProducto, name='editarProducto'),
    path('eliminar/<int:id>', views.eliminarProducto, name='eliminarProducto'),
    path('editar/<int:id>', views.editarProducto, name='editarProducto'),
    path('registro/', views.registro, name='registro'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
