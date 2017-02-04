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
from Auth.views import contextCall,send_email,send_sms_single

server = "http://www.technex.in/"
sheetUrls = {
	"robowars":"https://script.google.com/macros/s/AKfycbx2vzxqBPhyG_107us9BAuESjk6vpKoCi1CMA5GIpdePy3oL04/exec",
	"pixelate":"https://script.google.com/macros/s/AKfycbzRrPLuk16hrDOIh7AmQViE7sJmdTX7Vq-w1WShHJbDg1Cjylo/exec",
	"hurdlemania":"https://script.google.com/macros/s/AKfycbwdqJGq0snCPSOL2vgRb0cxWUcTBOkBtp3Bk9zb2v615RxBb_k/exec",
	"mazeXplorer":"https://script.google.com/macros/s/AKfycbyymc9N9q3oXwJThjON78Swa3fnKwD9bXbEEGdNT49XWdmBbYU/exec",
	"open-software" : "https://script.google.com/macros/s/AKfycbxQeVLQzJ-l0HGdrovmvKRfStBmmrXzJlk5detmE6N037BzBAc6/exec",
	"open-hardware": "https://script.google.com/macros/s/AKfycbwE6p7LyUHApX7oTnsmiR-Vk_Q2x1YJQd5fYcfn9bTjfLq35Wg/exec",
	"green-tech": "https://script.google.com/macros/s/AKfycbxPWMx8KBwuNLcBeG23QCaZX7FJ5lOAjStMxQ15S4z57X2xEUQ/exec",
	"capture-the-flag" : "https://script.google.com/macros/s/AKfycby4I0Ve0lZVQkPbUk-Fzn-ik0gpZ0FYapfz8k30GmjcOVZxiNk/exec",
	"appathon": "https://script.google.com/macros/s/AKfycbwppdd0aJyK6GD9VmmvlvsqSrr0LyjteBalFRMRWiFBTDqtqA2S/exec",
	"international-coding-marathon": "https://script.google.com/macros/s/AKfycbxmIEJ-gdZOyvpAKm84L3eeMOnyavujg5kvLcj2jR7ctm1EqxY/exec",
	"mlware": "https://script.google.com/macros/s/AKfycbwfyM7gZ26iI17kQslhnw_1G_621t-XeDeuY8LBBcXiqN8ELHi_/exec",

	"economists-enigma": "https://script.google.com/macros/s/AKfycbxMmy7yjzvDmLY83zkM--P86XVgnryuBkrJUuhM1C4XDY0qjm3z/exec",
	"manthan": "https://script.google.com/macros/s/AKfycbwe6tPsgigg6-SX1WyUo00RQXM__tJh_01MNLBs5csQx2BC4HI/exec",
	"krackat": "https://script.google.com/macros/s/AKfycbz6GS25vFDJsY02mX749TjC2YSnrXdvCcVZs5LWoaNbhGv_f6H0/exec",
	"bulls-floor": "https://script.google.com/macros/s/AKfycbxucNiOHRGcshykqMiTgHdV7uCc3JkifXgsfPDReX-41-VkfAM/exec",
	"analiticity": "https://script.google.com/macros/s/AKfycbxmDxWFuRA2PBu6e2GefsmeOPx4Q2inXbNHprheGUVn1XFa7h6A/exec",

	"2d":"https://script.google.com/macros/s/AKfycbwf1qvqJwVLgRNnD_JhZROI2r2AIrlOrTlxRAzAWRccS5pQerY/exec",
	"animaze":"https://script.google.com/macros/s/AKfycbxS-q0nnu3BfadEq-QWU_KuR8v2FMk5Ji40Y3gBDHGmZ_E9n_s/exec",
	"avant-garde":"https://script.google.com/macros/s/AKfycbzbMnYK0LUapV-62CKM3GrA61z8nEmPzJDnhbtUY2cXgQGX5vU/exec",
	"iso":"https://script.google.com/macros/s/AKfycbxM9pEcYkjnFKMVWoRCAy_HayzgLuxaXDDD-ccGGkCi_Qgz2xw/exec",
	"collage":"https://script.google.com/macros/s/AKfycbx-ElC8fhlP5h2lZucFVF01BzdMaPMW6GrsHfotZGYg-SOs_4Gj/exec",
	"minimize":"https://script.google.com/macros/s/AKfycbwYTV5c6Yw5MRy1OxII-U6A78YsWz_iNqFqIzlS_eb6NJ408tY/exec",
	"exploring-interstellar":"https://script.google.com/macros/s/AKfycbywyOuIP8aGFaCXhrhAtP8bmhV6KIyfnIcwWjnBe6nmVsycAPA/exec",
	"astroquiz":"https://script.google.com/macros/s/AKfycbzAiILENMWurTcDePvF0_TRx3n57M7uGVOJ5lwMlMf48bQGQDmt/exec",
	"astrophotography":"https://script.google.com/macros/s/AKfycbzrihE1zlcubi_u8Jk6sZryUgH1NCyBlktsdcL-zQUJqB4V158/exec",
	"scientists-utopia":"https://script.google.com/macros/s/AKfycbwIPTv_aNfvOqn4EVi8LKJoOsI9xmGiv6fzU8hoNUekT1djVK5Z/exec",
	"aagaz":"https://script.google.com/macros/s/AKfycbxnmQC1co_4hTsHYUlB2mhl0wVIG67hdGkIHTxUmtC6s4gpFSQi/exec",
	"sampann":"https://script.google.com/macros/s/AKfycbza0JY7Zl1-1Rp7WhtpzMHRdiX4A0aaVUMY_Ly9dExcC2QZxi77/exec",
	"swachch":"https://script.google.com/macros/s/AKfycbyiLuidIIPe8q1Cc2JRctAYg7GuTb0ilRdB2U288cC6kgQcGFQF/exec",
	"vision":"https://script.google.com/macros/s/AKfycbynUPef4u0AqxuGIaR_0_m35Ry6-KipzRkkQngaGjuTSuPupAU/exec",
	"greenx":"https://script.google.com/macros/s/AKfycbzqPHVP19tDZaru1DBvp2GER_Ac9sXfwCKXakY2vj7ynwWZC_g/exec",

	"drone-tech": "https://script.google.com/macros/s/AKfycbz6q2nFTvqrFky8ehK0H7Lavig-K9it8eky6r3o0g5W8Efc__F0/exec",
	"daeroglisseur": "https://script.google.com/macros/s/AKfycbwNMPiqyEAMYJ2D9LEkpY-35HOtx7CuoiLRL86vxSQkqRLFYbo/exec",
	"la-trajectoire":"https://script.google.com/macros/s/AKfycbyA7f6YhOCEBxDas3pkKuVj7f_l-wqMwMl7reNJy3DpG3kR0mE/exec",
	"momentum":"https://script.google.com/macros/s/AKfycbwhENBDBnaEWYTJw-3opilMvz6BPGi3H3rR4f28Okp1IYNBSbE/exec",

	"axelerate": "https://script.google.com/macros/s/AKfycbyKHb2ZmZ1UF8LId4ICMveb2ygx5cojpvNre8I5lju8ACjhQBxI/exec",
	"goldbergs-alley": "https://script.google.com/macros/s/AKfycbyFAD8X7_ePW5ficdgcWPZ_obpxuly-5UAX26W9lj5VCJMTxZw/exec",
	"bridgeit": "https://script.google.com/macros/s/AKfycby99ACnseBDFL7y2cmarSNrhIvzcHllw4SfHr4ovh0iHoBId-M/exec",
	"hydracs": "https://script.google.com/macros/s/AKfycbz8bZZxxjZVIqS9virOgox90WmLjvGz0RK3m8cr9fv9q6BbpbY/exec",


}

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
			message=" Team Registration successful for team name "+ str(team.teamName) + " . Visit www.fb.com/technex for updates. \nRegards\nTeam Technex"
			send_sms_single(message,str(teamLeader.mobileNumber))
			for user in users:
				send_email(user.email,subject,body%(user.user.first_name,event.eventName.capitalize(),team.teamName,teamLeader.email,memberEmails))
			response['status'] = 1
			spreadsheetfill_register(team)
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
		if 1:#try:
			print data['identifier']
			team = Team.objects.get(teamLeader = request.user.techprofile,technexTeamId = data['identifier'])
			spreadsheetfill_delete(team)
			send_email("events@technex.in","Team Delete Mail",str(str(team.technexTeamId)+"  "+team.event.eventName+"  "+team.teamName))
			team.delete()
			response['status'] = 1
		else:#except:
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


def spreadsheetfill_register(team):
	members = team.members.all()
	#print members[0].email.encode("utf-8")
	#print members[0].college.collegeName
	#for m in team.members.all():
	#	members.append(m.email.encode("utf-8"))
	dic = {
	"teamName":team.teamName,
	"leaderEmail":team.teamLeader.email,
	"leaderMobile":str(team.teamLeader.mobileNumber),
	"leaderCollege":team.teamLeader.college.collegeName,
	"teamId":team.technexTeamId
	}
	try:
		dic['member1'] = members[0].email.encode("utf-8")
		dic['college1'] = members[0].college.collegeName 
		dic['mobile1'] = members[0].mobileNumber
	except:
		dic['member1'] = 0
		dic['college1'] = 0
		dic['mobile1'] = 0
	try:
		dic['member2'] = members[1].email.encode("utf-8")
		dic['college2'] = members[1].college.collegeName
		dic['mobile2'] = members[1].mobileNumber
	except:
		dic['member2'] = 0
		dic['college2'] = 0
		dic['mobile2'] = 0
	try:
		dic['member3'] = members[2].email.encode("utf-8")
		dic['college3'] = members[2].college.collegeName
		dic['mobile3'] = members[2].mobileNumber
	except:
		dic['member3'] = 0
		dic['college3'] = 0
		dic['mobile3'] = 0
	try:
		dic['member4'] = members[3].email.encode("utf-8")
		dic['college4'] = members[3].college.collegeName
		dic['mobile4'] = members[3].mobileNumber
	except:
		dic['member4'] = 0
		dic['college4'] = 0
		dic['mobile4'] = 0
	print dic
	url = sheetUrls[team.event.nameSlug.encode("utf-8")]
	requests.post(url,data=dic)
 	
def spreadsheetfill_delete(team):
	#members = team.members.all()
	#print members[0].email.encode("utf-8")
	#print members[0].college.collegeName
	#for m in team.members.all():
	#	members.append(m.email.encode("utf-8"))
	dic = {
	"teamName":team.teamName,
	"leaderEmail":team.teamLeader.email,
	"leaderMobile":str(team.teamLeader.mobileNumber),
	"leaderCollege":team.teamLeader.college.collegeName,
	"teamId":team.technexTeamId,
	"teamDelete":1
	}
	print dic
	url = sheetUrls[team.event.nameSlug.encode("utf-8")]
	requests.post(url,data=dic)
