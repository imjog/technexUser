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
	url(r'^dashboard/$', genetella,name='dashboard'),
	#url(r'^logout/$', logoutView,name='logout'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/register'}),
	url(r'^fbConnect/$', fbConnect,name='fbConnect'),
	url(r'^resetPass/(?P<key>[\w\-]+)/$', resetPass, name='resetPass'),
	url(r'^$',IndexView,name='home'),
	url(r'^talks/', guestLecture, name='guestLecture'),
	url(r'^contacts/',team,name='teamPage'),
	url(r'^checkEmail/',emailUnique,name='emailUnique'),
	url(r'^botApi/',botApi,name='botApi'),
	url(r'^sponsors/',sponsors,name='sponsors'),
	url(r'^ca/',ca,name='ca'),
	#url(r'^dashboardDummy/', dummyDashboard, name='Apparent Dashboard'),
	url(r'^forgotPassword/$',forgotPassword, name='forgot Password'),

	url(r'^resetPass/(?P<forgotPassKey>[\w\-]+)/$', resetPass, name='resetPass'),
	url(r'^cdncheck/$', cdncheck, name='cdncheck'),
	url(r'^updateProfile/',profileData,name='profile edit'),
    url(r'^resetpassword/',changePass,name='change password'),
    url(r'^startupregister/',startUpRegistration,name='startup registeration'),
    url(r'^startupfair/',startupFair,name='startup Fair'),
    url(r'^workshopRegister/',workshopRegister,name='workshopRegister'),
    url(r'^botTest/',botTest,name='bot Test'),
	#url(r'^genetella/',genetella, name='Mission Dashboard'),
	#url(r'^fb/$',demofb_id,name='demofb_id'),
	# url(r'^collegejson/$', CollegeSearch, name='api_register'),

	#url(r'^$', IndexView, name= 'index'),

	#url(r'^logout/$', LogoutView, name='logout'),
	url(r'^googlec0c9e6f96a842b6d.html/',gverify,name='gverify'),
	
]
