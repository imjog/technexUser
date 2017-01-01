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
from Auth.views import contextCall,send_email

server = "http://www.technex.in/"


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
			return JsonResponse(response)
	else:
		response['status'] = 0
		return render(request, 'eventRegistration.html',contextCall(request))
		#return JsonResponse(response)


def teamLeave(request):
	response = {}
	if request.method == 'POST':
		data = request.POST #json.loads(request.body)
		print data
        try:
        	team = Team.objects.get(teamId = data['identifier'])
        	team.members.remove(request.user.techprofile)
        	response['status'] = 1
        except:
        	response['status'] = 0
		return JsonResponse(response)
	else:
		response['status'] = 0
		response['error'] = 'Invalid request'
		return JsonResponse(response)

@csrf_exempt
def teamDelete(request):
	response = {}
	if request.method == 'POST':
		data = json.loads(request.body)
		try:
			print data['identifier']
			team = Team.objects.get(teamLeader = request.user.techprofile,technexTeamId = data['identifier']).delete()
			response['status'] = 1
		except:
			response['status'] = 0
		return JsonResponse(response)
	else:
		response['status'] = 0
		response['error'] = 'Invalid request'			
		return JsonResponse(response)

def memberDelete(request):
	response = {}
	if request.method == 'POST':
		data = request.POST
		if True:
			member = TechProfile.objects.get(email = data['identifier'])
			team = Team.objects.get(teamLeader = request.user.techprofile, teamId = data['teamId'])
			team.members.remove(member)
			response['status'] = 1
		else:
			response['status'] = 0
		return JsonResponse(response)
	else:
		response['status'] = 0
		response['error'] = 'Invalid request'
		return JsonResponse(response)

#@login_required('/')
def event(request):
	if request.method == 'POST':
		print request.POST['members']
		return HttpResponse(request.body)
	else:
		return render(request, 'eventRegistration.html')

'''
def spreadsheetfill_register(team):
	
	dic = {
	'name' : team.teamName,
	'teamId' : team.technexTeamId,
	'teamLeader' : techprofile.college.collegeName,
	'technexId' : techprofile.technexId,
	'year' : techprofile.year,
	'mobileNumber': techprofile.mobileNumber,
	'city' : techprofile.city,
	}

	url = 'https://script.google.com/macros/s/AKfycbzYXljFklasr5Mx6wHtD_Jc2wONXuqumDTRJ1rM3oMR2MDySiAr/exec'
	requests.post(url,data=dic)
'''