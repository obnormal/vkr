"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import HttpResponseRedirect
from django.contrib import admin
# from django.shortcuts import redirect
from django.urls import path, include
# from two_factor.urls import urlpatterns as tf_urls

from untitled import settings, views
from django.conf.urls.static import static
# from market import views

urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('market/', include('market.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.user_page, name='user-page'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('aa/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
