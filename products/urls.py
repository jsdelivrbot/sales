from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'products'

urlpatterns  = [
	#url(r'^$', views.index, name='list_samples'),
	url(r'^create/$', login_required(views.create), name='create'),
	url(r'^list/$', login_required(views.list), name='list'),
	url(r'^list_json$', login_required(views.ListJson.as_view()), name='list_json'),
]