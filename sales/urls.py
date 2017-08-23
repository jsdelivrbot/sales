"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from home import views as home_views

urlpatterns = [
	url(r'^$', home_views.home, name='home_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),
    url(r'^productsales/', include('productsales.urls')),
    url(r'^login/', home_views.login_page, name='login_page'),
	url(r'^login_attempt/', home_views.login_attempt, name='login_attempt'),
	url(r'^logout/', home_views.logout, name='logout'),
]