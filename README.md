# TECHNEX

# Api Documentation
## Registration Api
<br> <br>
Url: http://technex-ca.herokuapp.com/api/register
<br>
Method: POST
<br>
Json object Expected : 			//(all fields required)<br>
								{<br>
									"email" : emailOfUser,<br>
									"name" : firstName,<br>
									"password" : password,<br>
									"college" : collegeName,<br>
									"year" : year(1,2,3,4,5)<br>
									"mobile_number" : mobileNumber<br>
								 }<br><br>

Json Response for Successful registration:<br>
								{<br>
								 	"status" : "Profile created successfully"<br>
								}<br><br>


Json Response for Invalid Request(requests other than post):<br>
								{<br>
									"Error" : True,<br>
									"status" : "invalid request,Post request Please!"<br>
								}<br><br><br>

## Login Api
<br><br>
Url: http://technex-ca.herokuapp.com/api/login
<br>
Method: POST
<br>
Json object Expected:<br>			{<br>
									"email" : email,<br>
									"password" : password<br>
								}<br><br>

Json Response for successful Login: <br>
								{<br>
									"status" : "logged in"<br>
								}<br><br>

Json Response for wrong Username/password:<br>
								{<br>
									"Error" : True,<br>
									"status" : "Invalid Credentials!"<br>
								}<br>


## Event Api
<br><br>
Url: https://technexuser.herokuapp.com/api/eventApi
<br>
Method: GET/POST
<br>
*No parameter Expected*
<br>
Json Response :{<br>
					
					"data":[
					{
					"name":parentEventName,
					"description":parentEventDescription,
					"events":[
					{
					"eventName":eventName,
					"eventDescription":eventDescription,
					"deadLine":deadLineOfEvent,
					"prizeMoney":prizeMoney,
					"maxMembers":maxmimNumberOfMembersAllowedInTeam,
					"eventOptions":[
					{
					"optionName":optionName,
					"optionDescription":optionDescription,
					}
					]
					}
					]
					}
			
			
			]
			}

