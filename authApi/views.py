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
from Events.views import spreadsheetfill_register
from django.core import serializers
from django.utils.crypto import get_random_string
server = "https://technexuser.herokuapp.com/"
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
    try:
        data =json.loads(request.body)
        #form = RegisterForm(data)
        email = data.get('email',None)
        try:
            techProfile = TechProfile.objects.get(email = email)
            #user = User.objects.get(email = email)
            #messages.warning(request,"Email Already Registered !")
            #return HttpResponse("Email Already Registered!") #redirect('/register')
            response['status'] = 2
            return JsonResponse(response)
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
            college = College.objects.get(collegeName = data.get('college').strip())
        except:
            college = College(collegeName = data.get('college').strip())
            college.save()
        try:
        	techprofile = TechProfile.objects.get(user = user)
        except:
			techprofile = TechProfile(user = user)
        techprofile.email = email
        techprofile.technexId = "TX"+str(10000+user.id)
        techprofile.college = college
        techprofile.mobileNumber = data.get('mobileNumber')
        techprofile.year = data.get('year')
        
		#print "codeBaes 2"
        pins = TechProfile.objects.all().values_list("pin")
        while True:
            stringR = get_random_string(3,allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            if stringR not in pins:
                techprofile.pin = stringR
                techprofile.save()
                break
        #range_start = 10**(n-1)
        #range_end = (10**n)-1
        #randint(range_start, range_end)
        #pin
        
        response['name'] = user.first_name
        response['mobileNumber'] = techprofile.mobileNumber
        response['year'] = techprofile.year
        response['college'] = techprofile.college.collegeName
        response['email'] = techprofile.email
        response['technexId'] = techprofile.technexId
        response['pin'] = stringR
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0 #For unknown error
        return JsonResponse(response)

@csrf_exempt
def ApiLoginView(request):
    response = {}
    if request.method == 'POST':

        post = json.loads(request.body)
        try:
            try:
                techProfile = TechProfile.objects.get(email = post['email'])
            except:
                techProfile = TechProfile.objects.get(technexId = post['email'])
        except:
            response['status'] = 0
            return JsonResponse(response)
        #user = authenticate(username = post['email'], email= post['email'], password = post['password'])
        kUser = techProfile.user
        user = authenticate(username = kUser.username, password = post['password'])

        if user is not None:
            if techProfile.apploginStatus is True:
                response['status'] = 3
                return JsonResponse(response)
            techProfile.apploginStatus = True
            techProfile.save()
            response['name'] = user.first_name
            response['mobileNumber'] = techProfile.mobileNumber
            response['year'] = techProfile.year
            response['college'] = techProfile.college.collegeName
            response['email'] = techProfile.email
            response['technexId'] = techProfile.technexId
            response['pin'] = techProfile.pin
            response['status'] = 1
            return JsonResponse(response)
        else:
            response['status'] = 0
            return JsonResponse(response)
    else:
        response['status'] = 2
        return JsonResponse(response)

@csrf_exempt
def logoutApi(request):
    
    response = {}
    try:
        post = json.loads(request.body)
        techProfile = TechProfile.objects.get(email = post['email'])
        techProfile.apploginStatus = False
        techProfile.save()
        response['status'] = 1
    except:
        response['status'] = 0 
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
                eventData['image'] = event.image
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

def send_email(recipient, subject, body):
    
    return requests.post(
        "https://api.mailgun.net/v3/mg.technex.in/messages",
        auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),
        data={"from": "No-reply <mailgun@mg.technex.in>",
              "to": recipient,
              "subject": subject,
              "text": body})

@csrf_exempt
def forgotPassword(request):
    response = {}
    if request.method == 'POST':
        post = json.loads(request.body)
        email = post.get("email")
        subject = "Reset Password"
        key = 'Technex'+email+"caportal"
        key = str(hash(key))
        try:
            user = User.objects.get(email = email)

        except:
            response['status'] = 0 # invalid email 
            return JsonResponse(response)
        try:
            forgotPass = ForgotPass.objects.get(user = user)
            forgotPass.key = key
            forgotPass.save()
        except:
            forgotPass = ForgotPass(user = user,key = key)
            forgotPass.save()
        body = "Please Cick on the following link to reset your Password.\n\n"
        body += server+"resetPass/"+key
        if send_email(email,subject,body):
            response['status'] = 1 # reset pass mail sent to email
            return JsonResponse(response)
        else:
            response['status'] = 2 # try again, network error
            return JsonResponse(response)

@csrf_exempt
def guestLectures(request):
    response = {}
    try:
        lectures = GuestLecture.objects.all()
        response['status'] = 1
        response['lectures'] = []
        for lecture in lectures:
            lectureData = {}
            lectureData['title'] = lecture.title
            lectureData['description'] = lecture.description
            lectureData['lecturerName'] = lecture.lecturerName
            lectureData['lecturerBio'] = lecture.lecturerBio
            lectureData['designation'] = lecture.designation
            lectureData['lectureType'] = lecture.lectureType
            lectureData['photo'] = lecture.photo
            response['lectures'].append(lectureData)
    except:
        response['status'] = 0 
    return JsonResponse(response)

@csrf_exempt
def workshopApi(request):
    response = {}
    try:
        workshops = Workshops.objects.all()
        response['status'] = 1
        response['workshops'] = []
        for workshop in workshops:
            workshopData = {}
            workshopData['title'] = workshop.title
            workshopData['image'] = workshop.image
            workshopData['description'] = workshop.description
            workshopData['dateTime'] = workshop.dateTime
            workshopData['workshopFees'] = workshop.workshopFees
            workshopData['order'] = workshop.order
            workshopData['workshopOptions'] = []
            workshopOptions = WorkshopOptions.objects.filter(workshop = workshop)
            for workshopOption in workshopOptions:
                workshopOptionData = {}
                workshopOptionData['optionName'] = workshopOption.optionName
                workshopOptionData['optionDescription'] = workshopOption.optionDescription
                workshopOptionData['optionOrder'] = workshopOption.optionOrder
                workshopData['workshopOptions'].append(workshopOptionData)
            workshopData['workshopOptions'].sort(key=lambda x: x['optionOrder'])
            response['workshops'].append(workshopData)
        response['workshops'].sort(key=lambda x: x['order'])
    except:
        response['status'] = 0
    return JsonResponse(response)

@csrf_exempt
def caEmailCount(request):
    response = {}
    post = request.POST
    if post['pass'] == 'bheenka':
        
        techProfiles = TechProfile.objects.filter(referral = post['email']).count()
        response['count'] = techProfiles
        response['status'] = 1
        return JsonResponse(response)
    else:
        response['status'] = 0
        return JsonResponse(response)

@csrf_exempt
def caEmailInfo(request):
    response = {}
    post = request.POST
    if post['pass'] == 'bheenka':
        techProfiles = TechProfile.objects.filter(referral = post['email'])
        response['count'] = techProfiles.count()
        response['info'] = []
        response['status'] = 1
        for techProfile in techProfiles:
            info = {}
            info['name'] = techProfile.user.first_name
            info['email'] = techProfile.email
            info['year'] = techProfile.year
            info['mobileNumber'] = techProfile.mobileNumber
            info['college'] = techProfile.college.collegeName
            info['city'] = techProfile.city
            response['info'].append(info)
        return JsonResponse(response)
    else:
        response['status'] = 0
        return JsonResponse(response)


@csrf_exempt
def eventRegistration(request):
    response = {}
     
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        event = Event.objects.get(nameSlug = data['eventSlug'])
        print "here"
        try:
            # print "here"
            team = Team.objects.get(teamName = data['teamName'], event = event)
            response['status'] = 0
            response['error'] = "TeamName Already exists"
            return JsonResponse(response)
        except:
            try:
                teamLeader = TechProfile.objects.get(technexId = data['teamLeaderEmail'])
            except:
                teamLeader = TechProfile.objects.get(email = data['teamLeaderEmail'])
            users = []
            # print "here"
            for member in data['members']:
                try:    
                    try:
                        user = TechProfile.objects.get(email = member)
                        users.append(user)
                    except:
                        user = TechProfile.objects.get(technexId = member)
                        users.append(user)
                except:
                    response['status'] = 0
                    response['error'] = 'Member not Registered('+member+')'
                    return JsonResponse(response)
                
            users = list(set(users))
            try:
                try:
                    team = Team.objects.get(teamLeader = teamLeader,event = event)
                    response['status'] = 0
                    response['error'] = 'You have Already registered for this event!!'
                    return JsonResponse(response)
                except:
                    team = Team.objects.get(event = event, members = teamLeader)
                    response['status'] = 0
                    response['error'] = 'You have Already registered for this event !!'
            except:
                for u in users: 
                    try:
                        try:
                            team = Team.objects.get(event = event, members = u)
                            response['status'] = 0
                            response['error'] = u.email+' Already registered for this event !!!'
                            return JsonResponse(response)
                        except:
                            team = Team.objects.get(event = event, teamLeader = u)
                            response['status'] = 0
                            response['error'] = u.email+' Already registered for this event !!!'
                            return JsonResponse(response)
                    except:
                        try:
                            if teamLeader == u:
                                users.remove(u)
                        except:
                            pass
                team = Team(teamLeader = teamLeader,event = event, teamName = data['teamName'])
                team.save()
                team.technexTeamId = "TM"+str(1000+team.teamId)
                team.save()
            subject = "[Technex'17] Successful Registration"
            body = '''
Dear %s,

Thanks for registering for %s Technex'17.

Your Team Details Are
Team Name- %s
Team Leader- %s
Team Members- %s


An important note to ensure that the team can contact you further:  If you find this email in Spam folder, please right click on the email and click on 'NOT SPAM'.


Note : As this is an automatically generated email, please don't  reply to this mail. Please feel free to contact us either through mail or by phone incase of any further queries. The contact details are clearly mentioned on the website www.technex.in. 
              

Looking forward to seeing you soon at Technex 2017.

All the best!


Regards

Team Technex
Regards
            '''
            memberEmails = ""
            for user in users:
                memberEmails += user.email+'  ' 
                team.members.add(user)
            send_email(teamLeader.email,subject,body%(teamLeader.user.first_name,event.eventName.capitalize(),team.teamName,teamLeader.email,memberEmails))
            for user in users:
                send_email(user.email,subject,body%(user.user.first_name,event.eventName.capitalize(),team.teamName,teamLeader.email,memberEmails))
            response['status'] = 1
            spreadsheetfill_register(team)
            return JsonResponse(response)
    else:
        response['status'] = 0
        return JsonResponse(response)


@csrf_exempt
def startUpFairApi(request):
    response = {}
    try:
        djangoArray = StartUpFairData.objects.all()
        data = []
        for djangoObject in djangoArray:
            dataObject = {}
            dataObject['introduction'] = djangoObject.introduction
            dataObject['content'] = djangoObject.content
            data.append(dataObject)
        response['data'] = data
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0
        return JsonResponse(response)

@csrf_exempt
def exhibitionsApi(request):
    response = {}
    try:
        djangoArray = Exhibitions.objects.all()
        data = []
        for djangoObject in djangoArray:
            dataObject = {}
            dataObject['introduction'] = djangoObject.introduction
            dataObject['content'] = djangoObject.content
            data.append(dataObject)
        response['data'] = data
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0
        return JsonResponse(response)

@csrf_exempt
def pronitesApi(request):
    response = {}
    try:
        djangoArray = Pronites.objects.all()
        data = []
        for djangoObject in djangoArray:
            dataObject = {}
            dataObject['introduction'] = djangoObject.introduction
            dataObject['content'] = djangoObject.content
            data.append(dataObject)
        response['data'] = data
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0
        return JsonResponse(response)

@csrf_exempt
def instituteDayApi(request):
    response = {}
    try:
        djangoArray = InstituteDay.objects.all()
        data = []
        for djangoObject in djangoArray:
            dataObject = {}
            dataObject['introduction'] = djangoObject.introduction
            dataObject['content'] = djangoObject.content
            data.append(dataObject)
        response['data'] = data
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0
        return JsonResponse(response)

@csrf_exempt
def corporateConclaveApi(request):
    response = {}
    try:
        djangoArray = CorporateConclave.objects.all()
        data = []
        for djangoObject in djangoArray:
            dataObject = {}
            dataObject['introduction'] = djangoObject.introduction
            dataObject['content'] = djangoObject.content
            data.append(dataObject)
        response['data'] = data
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0
        return JsonResponse(response)

@csrf_exempt
def hospitalityApi(request):
    response = {}
    try:
        djangoArray = Hospitality.objects.all()
        data = []
        for djangoObject in djangoArray:
            dataObject = {}
            dataObject['introduction'] = djangoObject.introduction
            dataObject['content'] = djangoObject.content
            data.append(dataObject)
        response['data'] = data
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0
        return JsonResponse(response)

