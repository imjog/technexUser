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
#from Auth.forms import *
# Create your views here.
def contextCall(request):
    response = {}
    try:
        user = request.user
        techprofile = user.techprofile
        response['user'] = user
        response['techProfile'] = techprofile
    except:
        pass
    return response
@csrf_exempt
def ApiRegisterView(request):
    response = {}
    if request.user.is_authenticated():
        response['status'] = 3
        return JsonResponse(response)
    if True:
        data =json.loads(request.body)
        #form = RegisterForm(data)
        email = data.get('email',None)
        try:
            user = User.objects.get(email = email)
            response['status'] = 2 #for already registered
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
        response['name'] = newUser.first_name
        response['mobileNumber'] = techprofile.mobileNumber
        response['year'] = techprofile.year
        response['college'] = techprofile.college.collegeName
        response['email'] = newUser.email
        response['status'] = 1
        return JsonResponse(response)
    else:
        response['status'] = 0 #For unknown error
        return JsonResponse(response)

@csrf_exempt
def ApiLoginView(request):
    response_data = {}
    if request.user.is_authenticated():
        response_data['status'] = 3
        return JsonResponse(response_data)
    try:
        data = json.loads(request.body)
        #form = LoginForm(data)
        if True:
            email = data.get('email',None)
            password = data.get('password',None)
            user = authenticate(username=email, email=email, password=password)
            if user is not None:
                login(request, user)
                response_data['status'] = 1
                response_data['name'] = user.first_name
                response_data['email'] = user.email
                techprofile = TechProfile.objects.get(user = user)
                response_data['mobileNumber'] = techprofile.mobileNumber
                response_data['year'] = techprofile.year
                response_data['college'] = techprofile.college.collegeName
                return JsonResponse(response_data)
            else:
                response_data['status'] = 0 #Invalid credentials
                return JsonResponse(response_data)
    except:
        response_data['status'] = 2 #email field not filled correctly
        return JsonResponse(response_data)

@csrf_exempt
@login_required(login_url='/api/eventApi') #not /login/
def logoutApi(request):
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
            pEventData['order'] = parentEvent.order
            pEventData['events'] = []
            events = Event.objects.filter(parentEvent = parentEvent)
            for event in events:
                eventData = {}
                eventData['eventName'] = event.eventName
                eventData['description'] = event.description
                eventData['deadLine'] = event.deadLine
                eventData['prizeMoney'] = event.prizeMoney
                eventData['maxMembers'] = event.maxMembers
                eventData['eventOrder'] = event.eventOrder
                eventData['eventOptions'] = []
                eventOptions = EventOption.objects.filter(event = event)
                for eventOption in eventOptions:
                    eventOptionData = {}
                    eventOptionData['optionName'] = eventOption.optionName
                    eventOptionData['optionDescription'] = eventOption.optionDescription
                    eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
                    eventData['eventOptions'].append(eventOptionData)
                pEventData['events'].append(eventData)
            response['data'].append(pEventData)
            response['status'] = 1
        return JsonResponse(response)
    except:
        response['error'] = True
        response['status'] = 'Error in finding events'
        return JsonResponse(response)

@csrf_exempt
def eventData(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        slug = data['parentEvent']
        try:
            parentEvent = ParentEvent.objects.get(nameSlug = slug)
        except:
            response['error'] = True
            response['status'] = 'Invalid Slug for Parent Event'
            return JsonResponse(response)
        response['name'] = parentEvent.categoryName
        response['description'] = parentEvent.description
        response['order'] = parentEvent.order
        response['events'] = []
        events = Event.objects.filter(parentEvent = parentEvent)
        for event in events:
            eventData = {}
            eventData['eventName'] = event.eventName
            eventData['description'] = event.description
            eventData['deadLine'] = event.deadLine
            eventData['prizeMoney'] = event.prizeMoney
            eventData['maxMembers'] = event.maxMembers
            eventData['eventOrder'] = event.eventOrder
            eventData['eventOptions'] = []
            eventOptions = EventOption.objects.filter(event = event)
            for eventOption in eventOptions:
                eventOptionData = {}
                eventOptionData['optionName'] = eventOption.optionName
                eventOptionData['optionDescription'] = eventOption.optionDescription
                eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
                eventData['eventOptions'].append(eventOptionData)
            response['events'].append(eventData)
        
        return JsonResponse(response)
    else:
        response['error'] = True
        response['status'] = 'Invalid Request'
        return JsonResponse(response)

@csrf_exempt
def parentEvents(request):
    response = {}
    if True:
        parentEvents = ParentEvent.objects.all()
        response['data'] = []
        for parentEvent in parentEvents:
            pEventData = {}
            pEventData['name'] = parentEvent.categoryName
            pEventData['description'] = parentEvent.description
            pEventData['order'] = parentEvent.order
            response['data'].append(pEventData)
        return JsonResponse(response)
    else:
        response['error'] = True
        response['status'] = 'Error getting Data!'
        return JsonResponse(response)

def register(request):
    if request.user.is_authenticated():
        return redirect('/dashboard')
    if request.method == 'POST':
        data = request.POST
        email = data.get('email',None)
        try:
            user = User.objects.get(email = email)
            messages.warning(request,"Email Already Registered !")
            return redirect('/register')
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
        techprofile = TechProfile(user = user)
        techprofile.college = college
        techprofile.mobileNumber = data.get('mobileNumber')
        techprofile.year = data.get('year')
        techprofile.save()
        #print "codeBaes 2"

        newUser = authenticate(username=email, password=password)
        login(request, newUser)
        return redirect('/dashboard')
    else:
        try:
            get = request.GET
            context = {
                        "name":get['name'],
                        }
            if 'email' in get:
                context['email'] = get['email']
            return render(request,'signup.html',context)
        except:
            return render(request,'signup.html')

def loginView(request):
    if request.user.is_authenticated():
        return redirect('/dashboard')
    if request.method == 'POST':
        post = request.POST
        try:
            user = User.objects.get(email = post['email'])
        except:
            messages.warning(request,"No User registered with the email!")
            return redirect('/login')
        user = authenticate(username = post['email'], email= post['email'], password = post['password'])
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.warning(request,"Invalid Credentials !")
            return redirect('/login')
    else:
        return render(request,'login.html')

@login_required(login_url='/login')
def dashboardView(request):
    context = contextCall(request)
    return render(request,'dashboard.html',context)

@csrf_exempt
@login_required(login_url='/login') #not /login/
def logoutView(request):
    logout(request)
    return redirect('/login')


def fbConnect(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        accessToken = post['accessToken']
        uid = post['uid']
        graph = facebook.GraphAPI(accessToken)
        args = {'fields':'name,email,picture'}
        profile = graph.get_object('me',**args)
        print profile
        try:
            fb_connect = FbConnect.objects.get(uid = uid)
            fb_connect.accessToken = accessToken
        except:
            fb_connect = FbConnect( accessToken = accessToken, uid = uid,profileImage = profile['picture']['data']['url'])
        fb_connect.save()
        try:
            user = User.objects.get(username = profile['email'])
            if  user.techprofile.fb is None:
                user.techprofile.fb = fb_connect
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            response['status'] = 1 #status for logged IN
        except:
            context = {}
            if 'name' in profile:
                context['name'] = profile['name']
            if 'email' in profile:
                context['email'] = profile['email']
            print context
            response['context'] = context
            response['status'] = 0 #status signup prepopulation of data
        return JsonResponse(response)
                

        
        
        
            
'''

def get_fb_token(app_id, app_secret):
    try:
        webbrowser.open('https://graph.facebook.com/oauth/authorize?'+urllib.urlencode({'client_id':'461359507257085','redirect_uri':'http://localhost:8000/','scope':'publish_actions'}))
    except:
        pass
    #secret_code = raw_input("Secret Code: ")
    payload = {'grant_type': 'client_credentials', 'scope':'user_likes,publish_actions', 'client_id': app_id, 'client_secret': app_secret,'redirect_uri':'http://localhost:8000/'}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    
    print file.text #to test what the FB api responded with
    #result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return file.text

def demofb_id(request):
    print str(request)
    app_id = '461359507257085'
    app_secret = '7be92fe7ee2c2d12cd2351d2a2c0dbb8'
    token = get_fb_token(app_id, app_secret)
    response = {}
    response['data'] = token
    #facebook.auth_url(app_id,'http://locahost:8000/ca/demofb_id',)
    return JsonResponse(response)
'''