# TECHNEX

# Api Documentation
## Registration Api
<br> <br>
Url: http://technexuser.herokuapp.com/api/register
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
									"mobileNumber" : mobileNumber<br>
								 }<br><br>

Json Response for Successful registration:<br>
								{<br>
								 	"status" : 1<br>
									"email" : emailOfUser,<br>
									"name" : firstName,<br>
									"college" : collegeName,<br>
									"year" : year(1,2,3,4,5)<br>
									"mobileNumber" : mobileNumber<br>
								}<br><br>


						
Json Response for Invalid Request(requests other than post):<br>
								{<br>
									
									"status" : 0
								}
Json Response if user already registered:<br>
					{<br>
					 	"status":2
					}
<br><br>

## Login Api
<br><br>
Url: http://technexuser.herokuapp.com/api/login
<br>
Method: POST
<br>
Json object Expected:<br>			{<br>
									"email" : email,<br>
									"password" : password<br>
								}<br><br>

Json Response for successful Login: <br>
								{<br>
									"status" : 1<br>
									"email" : emailOfUser,<br>
									"name" : firstName,<br>
									"college" : collegeName,<br>
									"year" : year(1,2,3,4,5)<br>
									"mobileNumber" : mobileNumber<br>
								}<br><br>

Json Response for wrong Username/password:<br>
								{<br>
									"status" : 0<br>
								}<br>
Json Response for Error in processing:<br>
						{
						"status":2
						}


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
					"status":1
		}

