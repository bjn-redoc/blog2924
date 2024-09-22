"""
URL configuration for blog2924 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve



urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    # fake admin
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('nothingisforever...!/', admin.site.urls),


    #path('admin/', admin.site.urls), # normal admin
    path('',include('blog.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    #path('members/', include('django.contrib.auth.urls')),     # /login, /logout, /register
    path('members/', include('members.urls')),
 ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
