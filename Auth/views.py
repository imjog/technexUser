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
from django_mobile import get_flavour
from user_agents import parse
#from Auth.forms import *
# Create your views here.
def ca(request):
    return redirect("http://ca.technex.in")
    
def sponsors(request):
    return redirect("http://16.technex.in/sponsors")

def team(request):
    teams = TeamList.objects.all()
    return render(request,"teamPage.html",{"teams":teams})

def IndexView(request):
    agent = parse(request.META['HTTP_USER_AGENT'])

    if(get_flavour(request) == 'full'):
        return render(request,"index.html",{'browser':agent.browser.family})
    else:
        return render(request,"mobile.html")
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

@login_required(login_url = '/login')
def dummyDashboard(request):
    context = contextCall(request)
    
    context['teamsAsMember'] = Team.objects.filter(members = context['techProfile'])
    context['teamsAsLeader'] = Team.objects.filter(teamLeader = context['techProfile'])
    print context
    return redirect('/events/register')#render(request, 'eventRegistration.html',context)

@csrf_exempt
def emailUnique(request):
    response = {}
    post = request.POST #json.loads(request.body)
    try:
        techProfile = TechProfile.objects.get(email = post['email'])
        #user = User.objects.get(email = post['email'])
        response = '0'
    except:
        response = '1'
    return HttpResponse(response)



def register(request):
    #if request.user.is_authenticated():
     #   return redirect('/dashboard')
    if request.method == 'POST':
        data = request.POST
        email = data.get('email',None)
        print 'code base 0'
        try:
            techProfile = TechProfile.objects.get(email = email)
            #user = User.objects.get(email = email)
            #messages.warning(request,"Email Already Registered !")
            return HttpResponse("Email Already Registered!") #redirect('/register')
        except:
            bugUsername = User.objects.latest('id').id
            user = User.objects.create_user(username=str(bugUsername+1))
            techprofile = TechProfile(user = user,email = email)
        user.first_name = data.get('name',None)
        password = data.get('password',None)
        user.set_password(password)
        user.save()
        print 'code base 1'
        try:
            college = College.objects.get(collegeName = data.get('college'))
        except:
            college = College(collegeName = data.get('college'))
            college.save()
        
        techprofile.college = college
        techprofile.mobileNumber = data.get('mobileNumber')
        techprofile.city = data.get('city')
        techprofile.year = data.get('year')
        if 'referral' in data:
            techprofile.referral = data['referral']
            print 'code base 1.5'
        print data.get('uid')
        try:
            fb_connect = FbConnect.objects.get(uid = data.get('uid'))
            techprofile.fb = fb_connect
            print data.get('uid')
            print 'code base1'
            techprofile.save()
        except:
            techprofile.save()
        print "codeBaes 2"
        subject = "[Technex'17] Confirmation of Registration"
        body = "Dear "+ data.get('name',None) +''',

You have successfully registered for Technex 2017. Team Technex welcomes you aboard!

An important note to ensure that the team can contact you further:  If you find this email in Spam folder, please right click on the email and click on 'NOT SPAM'.

       Our team will be at the task of updating you from time to time, the  information regarding the festival. Please keep visiting the website and the facebook page of Technex '17 to stay up-to-date with the latest happenings at Technex '17.


Note : As this is an automatically generated email, please don't  reply to this mail. Please feel free to contact us either through mail or by phone incase of any further queries. The contact details are clearly mentioned on the website www.technex.in. 
              

Looking forward to seeing you soon at Technex 2017.

All the best!


Regards

Team Technex.'''
        send_email(email,subject,body)
        #newUser = authenticate(username=email, password=password)
        #print 'code base 3'
        #login(request, newUser)
        return HttpResponse('1')
    else:
        context= {}
        context['all_colleges'] = College.objects.filter(status = True).values_list('collegeName',flat=True).distinct()
        try:
            get = request.GET
            context['name'] = get['name']
            context['uid'] = get['uid']            
            if 'email' in get:
                context['email'] = get['email']

            context['status'] = 1;
            return render(request,'signUp.html',context)
        except:
            context['status'] = 0;
            return render(request,'signUp.html',context)

def loginView(request):
    if request.user.is_authenticated():
        return redirect('/dashboard')
    if request.method == 'POST':
        post = request.POST
        try:
            techProfile = TechProfile.objects.get(email = post['email'])
        except:
            messages.warning(request,"No User registered with the email!")
            return redirect('/login')
        #user = authenticate(username = post['email'], email= post['email'], password = post['password'])
        kUser = techProfile.user
        user = authenticate(username = kUser.username, password = post['password'])
        
        if user is not None:
            login(request, user)
            return redirect('/dashboardDummy')
        else:
            messages.warning(request,"Invalid Credentials !")
            return redirect('/login')
    else:
        return render(request,'login.html')

@login_required(login_url='/login')
def dashboardView(request):
    context = contextCall(request)
    return render(request,'thankyou.html',context)

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
            techProfile = fb_connect.techprofile#TechProfile.objects.get(fb = fb_connect)
            user = techProfile.user #User.objects.get(username = profile['email'])
            #if  techProfile.fb is None:
            #   techProfile.fb = fb_connect
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            response['status'] = 1 #status for logged IN
        except:
            context = {}
            if 'name' in profile:
                context['name'] = profile['name']
            if 'email' in profile:
                context['email'] = profile['email']
            context['uid'] =  uid
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

@csrf_exempt
def resetPass(request,key):
    if request.method == 'GET':

        try:
            forgotPass = ForgotPass.objects.get(key = int(key))
            
            return render(request,"reset.html")
        except:
            messages.warning(request,'Invalid Url !')
            return redirect('/login')

    elif request.method == "POST":
        post = request.POST
        try:
            forgotPass = ForgotPass.objects.get(key=key)
            user = forgotPass.user
            password1 = post.get('form-password')
            password2 = post.get('form-repeat-password')
            if password1 == password2:
                forgotPass.delete()
                user.set_password(password1)
                user.save()
                messages.success(request,'password set successfully!',fail_silently=True)
                return redirect('/login')
            else:
                messages.warning(request,"passwords didn't match!")
                url = server+"/resetPass/"+key
                return redirect(request,url)
        except:
            raise Http404('Not allowed')


        return redirect('/resetPass/'+key)


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
def events(request):
    return render(request,'index2.html')

def event2api(request):
    return JsonResponse(response)


def event(request, key):
    response = {}
    if request.method == 'GET':
        
        
        try:
            parentEvent = ParentEvent.objects.get(nameSlug = key)
        except:
            response['error'] = True
            response['status'] = 'Invalid Slug for Parent Event'
            return JsonResponse(response)
        response['name'] = parentEvent.categoryName
        response['description'] = parentEvent.description
        response['order'] = parentEvent.order
        response['slug'] = parentEvent.nameSlug
        response['events'] = []
        events = Event.objects.filter(parentEvent = parentEvent)
        for event in events:
            eventData = {}
            eventData['eventName'] = event.eventName
            eventData['description'] = event.description
            # eventData['deadLine'] = event.deadLine
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
            eventData['eventOptions'].sort(key=lambda x: x['eventOptionOrder'])
            response['events'].append(eventData)
        response['events'].sort(key= lambda x: x['eventOrder'])  
        metaTags = MetaTags.objects.filter(event = parentEvent)
        #print json.dumps(response)
        return render(request,'index3.html',{'parentEvent':json.dumps(response), 'metaTags': metaTags})
    else:
        response['error'] = True
        response['status'] = 'Invalid Request'
        return JsonResponse(response)    

def guestLecture(request):
    response = {}
    resp = {}
    try:
        lectures = GuestLecture.objects.all()
        response['lectures'] = []
        for lecture in lectures:
            lectureData = {}
            lectureData['title'] = lecture.title.encode('ascii','ignore')
            lectureData['description'] = lecture.description.encode('ascii','ignore')
            lectureData['lecturerName'] = lecture.lecturerName.encode('ascii','ignore')
            lectureData['lecturerBio'] = lecture.lecturerBio.encode('ascii','ignore')
            lectureData['designation'] = lecture.designation.encode('ascii','ignore')
            lectureData['lectureType'] = lecture.lectureType.encode('ascii','ignore')
            lectureData['photo'] = lecture.photo.encode('ascii','ignore')
            response['lectures'].append(lectureData)
    except:
        response['status'] = 0  
    return render(request, 'guest.html', {'lectures':response})

def error404(request):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')

def send_email(recipient, subject, body):
    
    return requests.post(
        "https://api.mailgun.net/v3/mg.technex.in/messages",
        auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),
        data={"from": "Support Technex<support@technex.in>",
              "to": recipient,
              "subject": subject,
              "text": body})
@csrf_exempt
def botApi(request):
    response = {}
    post = request.POST
    if post['passkey'] == 'Xs6vvZdLhsYHAEK':
        try:
            user = User.objects.get(email = post['email'])
            response['status'] = 1
        except:
            response['status'] = 0
        techProfile = TechProfile.objects.get(user = user)
        techProfile.botInfo = post['uid']
        techProfile.save()
        
        return JsonResponse(response)
    return HttpResponse("Invalid Request!")