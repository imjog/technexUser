from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
import json
from Auth.models import *
#from Auth.forms import *
# Create your views here.


@csrf_exempt
def ApiRegisterView(request):
    response = {}
    data =json.loads(request.body)
    if True:
        #form = RegisterForm(data)
        email = data.get('email',None)
        try:
            user = User.objects.get(email = email)
            response['status'] = "Already Registered !!"
            return JsonResponse(response)
        except:
        	user = User.objects.create_user(username=email, email=email)
        user.first_name = data.get('name',None)
        password = data.get('password',None)
        user.set_password(password)
        user.save()
        try:
            college = College.objects.get(collegeName = data.get('college'))
        except:
            college = College(collegeName = data.get('college'))
            college.save()
        try:
        	techprofile = TechProfile.objects.get(user = user)
        except:
			techprofile = TechProfile(user = user)
        techprofile.college = college
        techprofile.mobileNumber = data.get('mobileNumber')
        techprofile.year = data.get('year')
        techprofile.save()
		#print "codeBaes 2"

        newUser = authenticate(username=email, password=password)
        login(request, newUser)

        response['status'] = "Profile created successfully"
        return JsonResponse(response)
    '''
    else:
        form = RegisterForm(data)
        for field in form:
            if field.errors:
                response_data[field.html_name] = field.errors.as_text()
                response_data['status'] = 'Error in registration'
        return JsonResponse(response_data)
    
	else:
        response_data['error'] = True
        response_data['status'] = 'invalid request,Post request Please!'
        return JsonResponse(response_data)
'''
@csrf_exempt
def ApiLoginView(request):
    response_data = {}
    data = json.loads(request.body)
    try:
        #form = LoginForm(data)
        if True:
            email = data.get('email',None)
            password = data.get('password',None)
            user = authenticate(username=email, email=email, password=password)
            if user is not None:
                login(request, user)
                response_data['status'] = 'logged in'
                return JsonResponse(response_data)
            else:
                response_data['error'] = True
                response_data['status'] = 'Invalid Credentials!'
                return JsonResponse(response_data)
    except:
        response_data['error'] = True
        response_data['status'] = "Please Fill the form correctly!"
        return JsonResponse(response_data)

@csrf_exempt
@login_required(login_url='/api/eventApi') #not /login/
def LogoutView(request):
    logout(request)
    response = {}
    response['status'] = "logged Out"
    return JsonResponse(response)



@csrf_exempt
def eventApi(request):
    response = {}
    try:
        parentEvents = ParentEvent.objects.all()
        response['data'] = []
        for parentEvent in parentEvents:
            pEventData = {}
            pEventData['name'] = parentEvent.categoryName
            pEventData['description'] = parentEvent.description
            pEventData['events'] = []
            events = Event.objects.filter(parentEvent = parentEvent)
            for event in events:
                eventData = {}
                eventData['eventName'] = event.eventName
                eventData['description'] = event.description
                eventData['deadLine'] = event.deadLine
                eventData['prizeMoney'] = event.prizeMoney
                eventData['maxMembers'] = event.maxMembers
                eventData['eventOptions'] = []
                eventOptions = EventOption.objects.filter(event = event)
                for eventOption in eventOptions:
                    eventOptionData = {}
                    eventOptionData['optionName'] = eventOption.optionName
                    eventOptionData['optionDescription'] = eventOption.optionDescription
                    eventData['eventOptions'].append(eventOptionData)
                pEventData['events'].append(eventData)
            response['data'].append(pEventData)
        return JsonResponse(response)
    except:
        response['error'] = True
        response['errorCode'] = 'Error in finding events'
        return JsonResponse(response)