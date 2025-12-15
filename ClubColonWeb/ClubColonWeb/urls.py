"""
URL configuration for ClubColonWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # 1. URL para el panel de administración de Django
    path('admin/', admin.site.urls),

    # 2. Inclusión CORRECTA de las URLs de la aplicación 'gestion'
    # Esto debe ser el único 'include' que apunte a 'gestion.urls'
    path('gestion/', include('gestion.urls', namespace='gestion')),

    # 3. Redirección de la raíz del sitio (/) a la página de inicio de la gestión.
    path('', lambda request: redirect('gestion:inicio'), name='root_redirect'),
]