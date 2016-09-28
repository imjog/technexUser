from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from authApi.views import *

app_name='authApi'

urlpatterns = [

	url(r'^login/$', ApiLoginView, name= 'api_login9'),
	#JsonResponse
	url(r'^register/$', ApiRegisterView, name='api_register9'),
	url(r'^forgotPass/$', forgotPassword, name='forgotPassword'),
	url(r'^eventData/$', eventData, name='eventData'),
	url(r'^parentEvents/$', parentEvents, name='parentEvents'),
	url(r'^eventApi/$', eventApi, name='eventApi'),
	url(r'^logout/$', logoutApi, name='logoutApi'),
]