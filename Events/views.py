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
from Auth.views import contextCall
server = "https://technexuser.herokuapp.com/"


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
			if 'teamLeaderTechnexId' in data:
				teamLeader = TechProfile.objects.get(technexId = data['teamLeaderTechnexId'])
			else:
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
			    team = Team.objects.get(teamLeader = teamLeader,event = event)
			except:
			    team = Team(teamLeader = teamLeader,event = event, teamName = data['teamName'])
			    team.save()
			for user in users:
			    team.members.add(user)
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


def teamDelete(request):
	response = {}
	if request.method == 'POST':
		data = request.POST
		try:
			team = Team.objects.get(teamLeader = request.user.techprofile, teamId = data['identifier']).delete()
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