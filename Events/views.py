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
server = "https://technexuser.herokuapp.com/"

@csrf_exempt
def eventRegistration(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        event = Event.objects.get(nameSlug = data['eventSlug'])
        try:
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
	        for member in data['members']:
	            if 'memberEmail' in member:
	                user = TechProfile.objects.get(email = member['memberEmail'])
	                users.append(user)
	            elif 'memberTechnexId' in member:
	                user = TechProfile.objects.get(technexId = member['memberTechnexId'])
	                users.append(user)
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
        return JsonResponse(response)


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