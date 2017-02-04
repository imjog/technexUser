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

Json Response for Already Logged in User:<br>
						{
						 "status":3
						 }
						 
		
## Logout Api
Url: https://technexuser.herokuapp.com/api/logout
Method: POST
Json Expected:
{"email":"email of user"}
Json on successful logout: {"status":1}
Json on failure or wrong email: {"status":0}


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


## Forgot Password Api
(UI not build till now although,it is totally functional)
<br><br>
Url: https://technexuser.herokuapp.com/api/forgotPass/
<br>
Method: POST
<br>
Json expected: <br>
			{<br>
			"email":email Of Registered User<br>
			}<br>
Json response if reset mail sent to your mail: <br>
			{<br>
			"status": 1 <br>
			}<br>

Json response if email given is not registered: <br>
			{<br>
			"status": 0 <br>
			}<br>
			
Json response for network error(try again in this case, althoug not likely to come): <br>
			{<br>
			"status": 2 <br>
			}<br>

## Event Registration Api
link:https://technexuser.herokuapp.com/api/eventReg/
Expected JSon:

{'eventSlug': 'robowars', 'members': ['memberEmail1 or TechnexId1','memberEmail2 or TechnexId2'], u'teamName': 'TeamName', 'teamLeaderEmail': 'b@b.com'}

SuccessFul Json Response:
{
"status":1
}

Error Response:
{
"status":0,
"Error":"Error Message"
}

## Workshop Api
url: https://technexuser.herokuapp.com/api/workshops/
Sample Response: {
  "status": 1,
  "workshops": [
    {
      "description": "Description",
      "title": "automobiles",
      "image": "",
      "workshopOptions": [],
      "dateTime": "2017-01-04T17:03:52Z",
      "workshopFees": 809099,
      "order": 1
    }
  ]
}

#guestLectureApi
url:https://technexuser.herokuapp.com/api/guestLecture/
Resposne:

{
  "lectures": [
    {
      "title": "-",
      "designation": "Senior Research Scientist-NASA",
      "lectureType": "-",
      "photo": "http://technex.in/static/assets/testimonial/rosley.png",
      "description": "<p>-</p>",
      "lecturerName": "Dr. Rosaly Lopes",
      "lecturerBio": "<p>Dr. Rosaly Lopes : Senior Research Scientist-NASA Dr. Rosaly Lopes-Gautier is one of NASA&rsquo;s leading planetary geologists and volcanologists. Born in Rio de Janerio, Brazil, she moved to England to do her B.Sc. in Astronomy from the University of London. In a career spanning Europe and the US, she was involved in fieldwork at several active volcanoes. She joined NASA&rsquo;s Jet Propulsion Laboratory in 1989, and has hence become an expert on Io and Titan, two moons of Jupiter. She has also worked extensively to disseminate knowledge on planetary geology through documentaries, books and public lectures; and has won several awards, including the 2005 Carl Sagan award and the 2007 NASA Exceptional Service medal.</p>"
    },
    {
      "title": "-",
      "designation": "Senior Researcher: IDSIA, Switzerland",
      "lectureType": "-",
      "photo": "http://technex.in/static/assets/testimonial/gianni%20di%20caro.png",
      "description": "<p>-</p>",
      "lecturerName": "Gianni di Caro",
      "lecturerBio": "<p>Gianni di Caro: Senior Researcher: IDSIA, Switzerland; Multi-Robot Network &amp; Swarm robotics Specialist. An inter-disciplinary researcher, Gianni di Caro is a senior researcher at IDSIA, Switzerland. An alumni of ULB, Brussels, he is currently involved in researching communications between and with large swarms of robots, particularly in the field of rescue operations. He has at various points worked on telecommunications, brain mapping, modelling the human immune system and in artificial intelligence. How work is highly cross-disciplinary in nature, as he researches natural examples such as ant swarms and their behavior to model networks and swarm robots.</p>"
    },
    {
      "title": "-",
      "designation": "MD & CEO :Futurebrands",
      "lectureType": "-",
      "photo": "http://technex.in/static/assets/testimonial/santoshdesai.png",
      "description": "<p>-</p>",
      "lecturerName": "Mr. Santosh Desai",
      "lecturerBio": "<p>Mr. Santosh Desai-MD &amp; CEO :Futurebrands , Ex-President: McCann Erickson. A marketing genius, boardroom titan and accidental writer, Santosh Desai is the MD &amp; CEO of Futurebrands ltd. An MBA holder from IIM Ahemdabad, he has worked in managerial and marketing positions in companies across the world. Prior to his current post, he worked as the President of McCann Erickson. Known for considering and understanding the impact of culture in people&rsquo;s choices, he became an expert in marketing and has since branched out to writing. His column &ldquo;City City Bang Bang&rdquo; is known for looking at society from an everyday viewpoint, and his first book, Mother Pious Lady, was released in 2015.</p>"
    },
    {
      "title": "-",
      "designation": "MD CEO Britannia",
      "lectureType": "-",
      "photo": "http://technex.in/static/assets/testimonial/vinitabali.png",
      "description": "<p>-</p>",
      "lecturerName": "Ms. Vinita Bali",
      "lecturerBio": "<p>Ms. Vinita Bali- MD CEO Britannia &amp; &quot;Businesswoman of the Year&quot; for 2009 by Economic Times. A long standing titan in the Indian business field, Vinita Bali was a graduate of LSR College, Delhi. She went on to do an MBA and have a diverse career ranging from interning at the UN and working as marketing and business strategy in several major brands. Her work as a marketer made brands such as Coca-Cola, Cadbury, Rasna and Britannia into household names across India, Africa, Latin America, China and Asia. Apart from being a clever marketer and strategist, she is also a tireless social worker whose work earned Britannia a Corporate Social Responsibility award. In 2009, Economic Times named her &quot;Businesswoman of the year&quot;.In 2011, Forbes named her one of &ldquo;Asia&rsquo;s 50 Power Businesswomen&rdquo;.</p>"
    },
    {
      "title": "-",
      "designation": "Lead Scientist- Hadron Collider-CERN High Energy",
      "lectureType": "-",
      "photo": "http://technex.in/static/assets/testimonial/atulgurtu.png",
      "description": "<p>-</p>",
      "lecturerName": "Mr. Atul Gurtu",
      "lecturerBio": "<p>Mr. Atul Gurtu :Lead Scientist- Hadron Collider-CERN High Energy Physicist: TIFR A renowned particle physicist, Atul Gurtu was the head of a 70-man team at the Large Hadron Collider in its early days. A graduate of Punjab University, he worked for four decades at the Tata Institute of Fundamental Research and joined CERN in testing the prototype LHC in the mid 90&rsquo;s. He worked for a short while as a distinguished professor at King Abdul Aziz university in Saudi Arabia. He has since retired.</p>"
    },
    {
      "title": "-",
      "designation": "Editorial Director: The New Indian Express",
      "lectureType": "-",
      "photo": "http://technex.in/static/assets/testimonial/prabhuchawla.png",
      "description": "<p>-</p>",
      "lecturerName": "Mr. Prabhu Chawla",
      "lecturerBio": "<p>Mr. Prabhu Chawla- Editorial Director: The New Indian Express, Anchor of &ldquo;Seedhi Baat&rdquo;. Prabhu Chawla is the Editorial Director of The New Indian Express. Earlier, he held the post of Editorial Director in the India Today magazine and the host of the popular Seedhi Baat programme on Aaj Tak. He holds the dubious honour of breaking an Indian Government with his daring expos&eacute; of the Jain Committee report. A Padma Bhushan awardee, his work in journalism earned him numerous awards from institutes all over the country.</p>"
    },
    {
      "title": "-",
      "designation": "DRDO",
      "lectureType": "-",
      "photo": "http://s3.amazonaws.com/37assets/svn/765-default-avatar.png",
      "description": "<p>-</p>",
      "lecturerName": "Milan Kumar Pal",
      "lecturerBio": "<p>Milan Kumar Pal is target system specialist scientist at&nbsp;DRDO.</p>"
    }
  ],
  "status": 1
}



## Short Apis
Response:
{"data":[{"introduction":"Intro",
"content":"content"}]
"status":1
}

Error Response:
{"status":0}

Urls:
https://technexuser.herokuapp.com/api/http/startUpFairApi/
https://technexuser.herokuapp.com/api/exhibitionsApi/
https://technexuser.herokuapp.com/api/pronitesApi/
https://technexuser.herokuapp.com/api/instituteDayApi/
https://technexuser.herokuapp.com/api/corporateConclaveApi/
https://technexuser.herokuapp.com/api/hospitalityApi/
