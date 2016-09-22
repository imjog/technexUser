from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from Auth.views import *

app_name='Auth'

urlpatterns = [

	#JsonResponse
	url(r'^api/login/$', ApiLoginView, name= 'api_login'),
	#JsonResponse
	url(r'^api/register/$', ApiRegisterView, name='api_register'),
	url(r'^api/eventApi/$', eventApi, name='eventApi'),
	url(r'^api/logout/$', logout, name='logoutApi'),
	url(r'^api/eventData/$',eventData, name='eventData'),
	url(r'^api/parentEvents/$',parentEvents, name='parentEvents'),
	
	# url(r'^collegejson/$', CollegeSearch, name='api_register'),

	#url(r'^$', IndexView, name= 'index'),

	#url(r'^logout/$', LogoutView, name='logout'),

]
