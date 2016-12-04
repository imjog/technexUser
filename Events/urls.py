from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from Events.views import *

app_name='Events'

urlpatterns = [

	url(r'^register/$', eventRegistration, name='eventRegistration'),
	url(r'^teamLeave/$', teamLeave, name='teamLeave'),
	url(r'^teamDelete/$', teamDelete, name='teamDelete'),
	url(r'^memberDelete/$', memberDelete, name='memberDelete'),
	#url(r'^register/$', event, name='event Reg'),
	
]