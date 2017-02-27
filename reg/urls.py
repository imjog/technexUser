from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from reg.views import *

app_name='reg'

urlpatterns = [

	url(r'register/$', offLineRegister, name="kaleidoscope"),
	url(r'main/$',intro,name='mainPage'),
	url(r'^details/$',details,name='details'),
	url(r'^hostel/$',hostelPortal,name='hostel'),
	url(r'^hostelChange/$',hostelAllot, name='Hostel Change'),
	url(r'createID/$',createIdCard,name = 'createID'),
	url(r'submitID/$',submitId,name = 'submitID'),
]