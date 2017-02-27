from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from payment.views import *

app_name='payment'

urlpatterns = [

	url(r'login/$', loginK, name="login"),
	url(r'logout/$',logoutK,name='logout'),
	url(r'payment/$',payment,name='mainPage'),
	url(r'paymentEnquiry/$',paymentEnquiry,name='paymentEnquiry'),
	url(r'deskTeamEnquiry/$',deskTeamEnquiry,name='deskTeamEnquiry'),
	url(r'hospi/$', hospi, name="hospi"),
	url(r'giveTshirt/$',giveTshirt,name='giveTshirt'),
	# url(r'refund/$',refund,name='idCard'),
	]