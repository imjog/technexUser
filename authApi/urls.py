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
	url(r'^guestLecture/$', guestLectures, name='guestLectures'),
	url(r'^eventRegistration/$', eventRegistration, name='eventRegistration'),
	url(r'^workshops/$', workshopApi, name='workshop'),
	url(r'^caEmailCount/$',caEmailCount,name='caEmailCount'),
	url(r'^caEmailInfo/$',caEmailInfo,name='caEmailInfo'),
	url(r'^startUpFairApi/$',startUpFairApi,name='startUpFairApi'),
	url(r'^exhibitionsApi/$',exhibitionsApi,name='exhibitionsApi'),
	url(r'^pronitesApi/$',pronitesApi,name='pronitesApi'),
	url(r'^instituteDayApi/$',instituteDayApi,name='instituteDayApi'),
	url(r'^corporateConclaveApi/$',corporateConclaveApi,name='corporateConclave'),
	url(r'^hospitalityApi/$',hospitalityApi,name='hospitality'),
	url(r'^notificationToken/$',notificationToken,name='notificationToken'),
]