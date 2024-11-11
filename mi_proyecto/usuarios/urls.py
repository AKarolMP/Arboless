# mi_proyecto/urls.py (o el nombre que le hayas dado al proyecto principal)
from django.contrib import admin
from django.urls import path
from usuarios.views import home, register_admin, admin_login, admin_dashboard  # Importa todas las vistas necesarias

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta del administrador de Django
    path('', home, name='home'),  # Página de inicio
    path('usuarios/register/', register_admin, name='register_admin'),  # Ruta para registrar admin
    path('usuarios/admin_login/', admin_login, name='admin_login'),  # Ruta para iniciar sesión
    path('usuarios/admin_dashboard/', admin_dashboard, name='admin_dashboard'),  # Ruta para el dashboard
]
