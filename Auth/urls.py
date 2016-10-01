from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from Auth.views import *

app_name='Auth'

urlpatterns = [

	#JsonResponse
	#url(r'^api/login/$', ApiLoginView, name= 'api_login'),
	#JsonResponse
	#url(r'^api/register/$', ApiRegisterView, name='api_register'),
	#url(r'^api/eventApi/$', eventApi, name='eventApi'),
	#url(r'^api/logout/$', logoutApi, name='logoutApi'),
	#url(r'^api/eventData/$', eventData, name='eventData'),
	#url(r'^api/parentEvents/$', parentEvents, name='parentEvents'),
	url(r'^register/$', register, name='register'),
	url(r'^login/$', loginView, name='login'),
	url(r'^events/$', events, name='event'),
	url(r'^events/(?P<key>[\w\-]+)/$', event, name='events'),
	url(r'^dashboard/$', dashboardView,name='dashboard'),
	url(r'^logout/$', logoutView,name='logout'),
	url(r'^fbConnect/$', fbConnect,name='fbConnect'),
	url(r'^resetPass/(?P<key>[\w\-]+)/$', resetPass, name='resetPass'),
	url(r'^guestLectures/', guestLecture, name='guestLecture'),
	#url(r'^fb/$',demofb_id,name='demofb_id'),
	# url(r'^collegejson/$', CollegeSearch, name='api_register'),

	#url(r'^$', IndexView, name= 'index'),

	#url(r'^logout/$', LogoutView, name='logout'),

]
