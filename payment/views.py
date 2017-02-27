from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
import requests
from django.views.decorators.csrf import csrf_exempt
import json
import os
import facebook
from Auth.models import *
#from payment.models import *
from django_mobile import get_flavour
from user_agents import parse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.staticfiles.templatetags.staticfiles import static
import dropbox
from django.db.models import Sum,Max
import urllib2
import cookielib
from ast import literal_eval
from xlrd import open_workbook
from xlwt import Workbook
import random
from django.utils.crypto import get_random_string
import cStringIO
from PIL import Image
import urllib
import cloudinary
import cloudinary.uploader
import cloudinary.api
import base64
from io import BytesIO
from django.core import serializers
# Create your views here.


def loginK(request):
	if request.method == 'POST':
		post = request.POST
		user = authenticate(username = post['username'],password = post['password'])
		if user is not None:
			login(request,user)
			#sessionBeginn(request)
			return redirect('/main/')
		else:
			return render(request,"login.html",{'errors':'Invalid credentials'})
	else:
		return render(request,'login.html')


@login_required(login_url = '/login')
@csrf_exempt
def payment(request):
	facilities = Facility.objects.all()
	if request.method == 'POST':
		post = request.POST
		facility = Facility.objects.get(name = post['facilityName'])
		try:
			techprofile = TechProfile.objects.get(email = post['identifier'])
		except:
			try:
				techprofile = TechProfile.objects.get(technexId = post['identifier'])
			except:
				return render(request,'payment.html',{'errors':'Invalid Email or TechnexId','facilities':facilities})

		if post['amount'] > 0:
			transaction = Transaction(creditor = techprofile,amount = post['amount'], facility = facility, reciever = request.user.deskteam)
			transaction.save()
			#transactionsSessions = request.session['transactions']
			#transactionsSessions.append(transaction.id)
			#request.session['transactions'] = transactionsSessions
			recheckTransaction = Transaction.objects.filter(id = transaction.id)
			datas = json.loads(serializers.serialize('json',recheckTransaction,fields = ('amount','timeStamp')))
			datas[0]['fields']['creditor'] = recheckTransaction[0].creditor.user.first_name
			datas[0]['fields']['facility'] = recheckTransaction[0].facility.name
			datas[0]['fields']['reciever'] = recheckTransaction[0].reciever.user.first_name
			response = {}
			response['transaction'] = datas[0]['fields']
			return JsonResponse(response) #render(request,'payment.html',{'transaction':recheckTransaction,'facilities':facilities})
		else:
			return render(request,'payment.html',{'error':'Invalid Transaction','facilities':facilities})
	else:
		return render(request,'payment.html',{'facilities':facilities})

# def 

def paymentEnquiry(request):
	if request.method == 'POST':
		post = request.POST
		try:
			techprofile = TechProfile.objects.get(email = post['identifier'])
		except:
			try:
				techprofile = TechProfile.objects.get(technexId = post['identifier'])
			except:
				return render(request,'enquiry.html',{'errors':'Invalid Email or TechnexId'})
		transactions = Transaction.objects.filter(creditor = techprofile)
		return render(request,'enquiry.html',{'transactions':transactions})	
	else:
		return render(request,'enquiry.html')

@login_required(login_url='/login')
def sessionBeginn(request):
	request.session['transactions'] = []


def logoutK(request):
	logout(request)
	#transactions = Transaction.objects.filter(id__in = request.session['transactions'])
	#request.session['transactions'] = []
	return redirect("/login") #,{'transactions':transactions})

def deskTeamEnquiry(request):
	#if request.user.deskteam.authorityLevel == 0:
	#	return redirect('/payment')
	try:
		if request.user.deskteam.authorityLevel != 1:
			return redirect('/main')
	except:
		pass
	deskteam = DeskTeam.objects.filter(authorityLevel = 0)
	transactionsData = []
	for deskteama in deskteam:
		transactionObject1 = {}
		transactions  = Transaction.objects.filter(reciever = deskteama).order_by('timeStamp')
		transactionArray = []
		count = 0
		for transaction in transactions:
			transactionObject = {}
			count += transaction.amount
			transactionObject['amount'] = transaction.amount
			transactionObject['facility'] = transaction.facility.name
			transactionObject['facilityPrice'] = transaction.facility.maxPrice
			transactionObject['creditor'] = transaction.creditor.email
			transactionObject['timeStamp'] = transaction.timeStamp
			transactionArray.append(transactionObject)
		transactionObject1['count'] = count
		transactionObject1['reciever'] = deskteama.user.username
		transactionObject1['data'] = transactionArray
		transactionsData.append(transactionObject1)
	for transactionData in transactionsData:
		for transactionB in transactionData['data']:
			print transactionB['amount']
			print transactionB['creditor']	
	print transactionsData
	return render(request,'deskEnquiry.html',{"transactionData":transactionsData})

def hospi(request):
	return render(request,'deskf.html')	

@csrf_exempt
def giveTshirt(request):
	response = {}
	post = request.POST
	try:
		techProfile = TechProfile.objects.get(email = post['identifier'])
	except:
		try:
			techProfile = TechProfile.objects.get(technexId = post['identifier'])
		except:
			response['status'] = 0 #Invalid Email/TechnexId 
			return JsonResponse(response)
	techProfile.idcard.tshirtStatus = True
	techProfile.idcard.save()
	response['status'] = 1
	return JsonResponse(response)
'''
@csrf_exempt
def refund(request):
	response = {}
	post = request.POST
	if 5:#try:
		idCard = IdCard.objects.get(pin = post['pin'])
		tech = idCard.techProfile
		
	else:#except:
		return render(request,'refund.html',{'errors':''})
'''