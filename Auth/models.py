from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.core.validators import URLValidator
import datetime
from django.utils import timezone
year_choices = [
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
        (6, 'Passout(Only for Startup Fair)'),
    ]

def get_user_image_folder(instance, filename):
    return "technexusers/%s-%s/%s" %(instance.user.first_name,instance.user.last_name, filename)


class College(models.Model):
    collegeId = models.AutoField(primary_key = True)
    collegeName = models.CharField(max_length=250)
    status = models.BooleanField(default = False)
    city = models.CharField(max_length=250,null = True, blank = True)
    state = models.CharField(max_length=250,null = True, blank = True)
    collegeWebsite = models.CharField(max_length = 250, default = '0')
    def __unicode__(self):
        return "%s - %s - %s - %s" %(self.collegeWebsite, self.collegeName, self.city, self.state)
class FbConnect(models.Model):
    uid = models.CharField(max_length = 200, null = True)
    accessToken = models.CharField(max_length = 250, null = True)
    profileImage = models.TextField(validators=[URLValidator()],blank=True,null = True)
    def __unicode__(self):
        return self.uid

        
class ParentEvent(models.Model):
    parentEventId = models.AutoField(primary_key = True)
    categoryName = models.CharField(max_length = 50)
    description = RichTextField(null = True,blank = True)
    order = models.SmallIntegerField(default = 0)
    sponimage=models.TextField(blank=True,null=True)
    sponlink=models.TextField(validators=[URLValidator()],blank=True,null = True)
    assosponimage=models.TextField(blank=True,null=True)
    assosponlink=models.TextField(validators=[URLValidator()],blank=True,null = True)    
    nameSlug = models.SlugField(null = True)
    def __unicode__(self):
        return self.categoryName

    
class Event(models.Model):
    eventId = models.AutoField(primary_key = True)
    eventOrder = models.SmallIntegerField(default = 0)
    eventName = models.CharField(max_length = 50)
    parentEvent = models.ForeignKey(ParentEvent)
    description = RichTextField(null = True,blank = True)
    deadLine = models.DateTimeField(null = True,blank = True)
    prizeMoney = models.IntegerField(null=True, blank=True)
    maxMembers = models.SmallIntegerField(null=True,blank=True)
    nameSlug = models.SlugField(null = True)
    abstract = models.SmallIntegerField(default = 0)
    image = models.TextField(validators=[URLValidator()], null = True, blank = True)
    def __unicode__(self):
        return self.eventName
        

class TechProfile(models.Model):
    class Meta:
        permissions = (
            ('permission_code', 'Publicity portal'),
        )
    user = models.OneToOneField(User)
    email = models.EmailField(max_length = 60,null = True, blank = True)
    technexId = models.CharField(max_length = 30,null = True,blank = True)
    year = models.IntegerField(choices=year_choices)
    mobileNumber = models.BigIntegerField()
    college = models.ForeignKey(College,null = True)
    fb = models.OneToOneField(FbConnect,null = True, blank = True)
    botInfo = models.CharField(max_length = 65,null = True, blank = True)
    city = models.CharField(max_length = 65,default = 'varanasi')
    referral = models.EmailField(max_length = 60, null = True, blank = True)
    pin = models.CharField(max_length= 20,null = True,blank = True)
    apploginStatus = models.BooleanField(default = False)
    #profile_photo = models.TextField(validators=[URLValidator()],blank=True)
    notificationToken = models.TextField(null = True,blank = True)
    tshirtdata = models.BooleanField(default = False)
    tshirtsize = models.CharField(max_length = 4, null = True , blank =True)
    color = models.CharField(max_length = 10 , null =True , blank = True)
    gender = models.CharField(max_length = 10, null = True , blank= True)
    arrivaldate = models.CharField(max_length = 15 , null =True , blank =True)
    confirmpart = models.ManyToManyField(Event , null = True ,blank =True)
    def __unicode__(self):
        return "%s -%s" %(self.user.first_name, self.college)




class Team(models.Model):
    teamName = models.CharField(max_length=50, null=True, blank=True)
    teamId = models.AutoField(primary_key = True)
    technexTeamId = models.CharField(max_length = 10, null = True, blank = True)
    event = models.ForeignKey(Event)
    teamLeader = models.ForeignKey(TechProfile,related_name = 'teamLeader')
    members = models.ManyToManyField(TechProfile,related_name = 'members',null = True)
    abstractstatus = models.SmallIntegerField(default = 0)
    def __unicode__(self):
        return self.teamName

class EventOption(models.Model):
    optionName = models.CharField(max_length = 50, null = True)
    optionDescription = RichTextField()
    eventOptionOrder = models.SmallIntegerField(default = 0)
    event = models.ForeignKey(Event)
    def __unicode__(self):
        return '%s %s'%(self.optionName,self.event)

class ForgotPass(models.Model):
    user = models.OneToOneField(User)
    key = models.CharField(max_length = 250)
    def __unicode__(self):
        return self.key

class GuestLecture(models.Model):
    title = models.CharField(max_length = 100)
    description = RichTextField()
    lecturerName = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    lecturerBio = RichTextField()
    lectureType = models.CharField(max_length = 100)
    photo = models.TextField(blank=True,null = True)
    def __unicode__(self):
        return '%s %s'%(self.title,self.lecturerName)


class PrimaryIndustry(models.Model):
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return '%s'%(self.name)

class BusinessType(models.Model):
    name = models.CharField(max_length = 3)
    def __unicode__(self):
        return '%s'%(self.name)
         

class Workshops(models.Model):
    workshopId = models.AutoField(primary_key = True)
    order  = models.SmallIntegerField(null = True)
    title = models.CharField(max_length = 100)
    description = RichTextField()
    dateTime = models.DateTimeField(null = True)
    workshopFees = models.IntegerField(null = True)
    maxMembers = models.SmallIntegerField(null = True)
    slug = models.SlugField(null = True)
    image = models.TextField(blank=True,null=True)
    sponimage=models.TextField(blank=True,null=True)
    sponlink=models.TextField(validators=[URLValidator()],blank=True,null = True)    

    def __unicode__(self):
        return '%s'%(self.title)

class WorkshopOptions(models.Model):
    optionName = models.CharField(max_length = 50, null = True)
    optionDescription = RichTextField()
    optionOrder = models.SmallIntegerField(null = True, blank = True)
    workshop = models.ForeignKey(Workshops)
    def __unicode__(self):
        return '%s %s'%(self.optionName, self.workshop)

class WorkshopTeam(models.Model):
    teamName = models.CharField(max_length=50, null=True, blank=True)
    teamId = models.AutoField(primary_key = True)
    workshop = models.ForeignKey(Workshops)
    teamLeader = models.ForeignKey(TechProfile,related_name = 'teamLeaderForWorkshop')
    members = models.ManyToManyField(TechProfile,related_name = 'members_for_workshop')

    def __unicode__(self):
        return '%s %s'%(self.teamName,self.teamLeader.user.first_name)

class MetaTags(models.Model):
    name = models.CharField(max_length = 50)
    content = models.TextField()
    event = models.ForeignKey(ParentEvent)
    def __unicode__(self):
        return '%s %s'%(self.name,self.event.categoryName)

class TeamList(models.Model):
    teamId = models.AutoField(primary_key = True)
    teamName = models.CharField(max_length = 50)
    order = models.SmallIntegerField(default = 0)
    def __unicode__(self):
        return self.teamName

class TeamMembers(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 65,null = True, blank = True)
    facebookLink = models.TextField(validators=[URLValidator()],blank=True,null = True)
    photo = models.TextField(validators=[URLValidator()],blank=True,null = True)
    designation = models.CharField(max_length = 50)
    number = models.BigIntegerField(null = True,blank = True)
    team = models.ForeignKey(TeamList)
    order = models.SmallIntegerField(default = 0)
    def __unicode__(self):
        return '%s %s'%(self.name,self.team.teamName)

class Notification(models.Model):
    notificationId = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 20)
    description = models.TextField(blank = True)
    time = models.DateTimeField(auto_now = True)
    photo = models.TextField(blank=True)

class ReaderStatus(models.Model):
    reader = models.ForeignKey(TechProfile)
    notification = models.ForeignKey(Notification)
    status = models.BooleanField(default = True)

class StartUpFair(models.Model):
    idea = models.CharField(max_length = 250, blank = True)
    interests = models.CharField(max_length = 500, null=True, blank = True)
    description = models.CharField(max_length = 20000, null=True, blank=True)
    year = models.SmallIntegerField(default = 0)
    angelListUrl = models.CharField(max_length = 200, null = True, blank = True)
    crunchBaseUrl = models.CharField(max_length = 200, null = True, blank = True)
    pindusry = models.ManyToManyField(PrimaryIndustry,related_name="primary_industry",null = True)
    bType = models.ManyToManyField(BusinessType,related_name="btype",null = True)  
    teamLeader = models.OneToOneField(TechProfile)
    teamName = models.CharField(max_length = 35)
    def __unicode__(self):
        return self.teamName

class StartUpMails(models.Model):
    email = models.EmailField(max_length = 65,unique = True)
    team = models.ForeignKey(StartUpFair)
    def __unicode__(self):
        return self.email    

class FbReach(models.Model):
    uid = models.CharField(max_length = 200, null = True)
    accessToken = models.CharField(max_length = 250, null = True)
    profileImage = models.TextField(validators=[URLValidator()],blank=True,null = True)
    def __unicode__(self):
        return self.uid

class PaymentStatusa(models.Model):
    tech = models.ForeignKey(TechProfile, null = True, blank = True)
    email = models.EmailField(max_length = 50, null = True, blank = True)
    status = models.CharField(max_length = 15)
    ticketId = models.CharField(max_length = 100)
    contact = models.CharField(max_length = 20,null = True,blank = True)
    ticketPrice = models.IntegerField(null = True,blank = True)
    timeStamp = models.CharField(max_length = 50,null = True,blank = True)
    ticketName = models.CharField(max_length = 65,null = True,blank = True)
    def __unicode__(self):
        return self.email

class SponsorshipType(models.Model):
    title = models.CharField(max_length  = 100)
    order = models.SmallIntegerField(default = 99)
    def __unicode__(self):
        return '%s %s'%(self.title,self.order)

class Sponsors(models.Model):
    sponsorType  = models.ForeignKey(SponsorshipType)
    order = models.SmallIntegerField(default = 999)
    name = models.CharField(max_length = 100)
    imageLink = models.TextField(validators=[URLValidator()],blank=True,null = True)
    websiteLink = models.TextField(validators=[URLValidator()],blank=True,null = True)
    def __unicode__(self):
        return '%s %s'%(self.name,self.order) 

class Way2smsAccount(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    messages_left=models.IntegerField(default=100)
    def __unicode__(self):
        return self.username

class Way2smsAccount_Premium(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    messages_left=models.IntegerField(default=100)
    def __unicode__(self):
        return self.username

class quiz(models.Model):
    quizId = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    activeStatus = models.SmallIntegerField(default = 0)
    def __unicode__(self):
        return self.name

class quizTeam(models.Model):
    teamId = models.AutoField(primary_key= True)
    quizTeamId = models.CharField(max_length = 10, null = True, blank = True)
    members = models.ManyToManyField(TechProfile , related_name = "quizMembers" , null = True)
    quizAttemptStatus = models.SmallIntegerField(default = 0)
    quiz = models.ForeignKey(quiz , null = True , blank = True)
    slot = models.SmallIntegerField(default = 0)
    def __unicode__(self):
        return self.quizTeamId

class quizTeam2(models.Model):
    teamId = models.AutoField(primary_key= True)
    quizTeamId = models.CharField(max_length = 10, null = True, blank = True)
    quizAttemptStatus = models.SmallIntegerField(default = 0)
    quiz = models.ForeignKey(quiz , null = True , blank = True)
    slot = models.SmallIntegerField(default = 0)
    member1Email = models.CharField(max_length = 65, null = True, blank = True)
    member2Email = models.CharField(max_length = 65, null = True, blank = True)
    member1Phone = models.CharField(max_length = 15, null = True, blank = True)
    member2Phone = models.CharField(max_length = 15, null = True, blank = True)
    name1 = models.CharField(max_length = 50, null = True, blank = True)
    name2 = models.CharField(max_length = 50, null = True, blank = True)
    status = models.BooleanField(default = False)
    key = models.CharField(max_length = 120, null = True, blank = True)
    def __unicode__(self):
        return self.member1Email

class questions(models.Model):
    questionId = models.AutoField(primary_key = True)
    quiz = models.ForeignKey(quiz, null = True)
    question = RichTextField(null = True,blank = True) #models.TextField(blank = True , null =True)
    integerAnswer = models.IntegerField(blank = True, null = True)
    def __unicode__(self):
        return '%s'%(self.questionId)            
'''
class grain(models.Model):
    optionId = models.AutoField(primary_key = True)
    optionText = models.TextField(blank = True, null = True)
    question = models.ForeignKey(questions)
    status = models.SmallIntegerField(default = 0)
'''    
class quizResponses(models.Model):
    responseId = models.AutoField(primary_key = True)
    quiz = models.ForeignKey(quiz, null = True)
    quizTeam = models.OneToOneField(quizTeam2)
    status = models.SmallIntegerField(default = 1)
    startTime = models.DateTimeField(auto_now = True,null = True, blank = True)
    questions = models.ManyToManyField(questions)
    def __unicode__(self):
        return '%s %s'%(self.quizTeam.quizTeamId,self.quiz.name)
    def validForSubmission(self,minutes):
        

        now = timezone.now()
        timediff = now - self.startTime
        print timediff.total_seconds()/60
        if timediff.total_seconds() > minutes*60:
            return False
        else:
            return True
    def timer(self):
        now = timezone.now()
        timediff = now - self.startTime
        return int(timediff.total_seconds())

'''
class questionResponses(models.Model):
    responseId = models.AutoField(primary_key = True)
    quiz = models.ForeignKey(quizResponses)
    option = models.ForeignKey(optionsC, null = True, blank = True)
    question = models.ForeignKey(questions, null = True, blank = True)
    integerAnswer = models.CharField(max_length = 20,null = True, blank = True)
    def __unicode__(self):
        return '%s'%(self.quiz.quiz.name)
'''
class StartupFairData(models.Model):
    introduction = models.CharField(max_length = 250, null = True, blank = True)
    content = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return '%s'%(self.introduction)

class Exhibitions(models.Model):
    introduction = models.CharField(max_length = 250, null = True, blank = True)
    content = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return '%s'%(self.introduction)

class Pronites(models.Model):
    introduction = models.CharField(max_length = 250, null = True, blank = True)
    content = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return '%s'%(self.introduction)

class InstituteDay(models.Model):
    introduction = models.CharField(max_length = 250, null = True, blank = True)
    content = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return '%s'%(self.introduction)

class CorporateConclave(models.Model):
    introduction = models.CharField(max_length = 250, null = True, blank = True)
    content = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return '%s'%(self.introduction)

class Hospitality(models.Model):
    introduction = models.CharField(max_length = 250, null = True, blank = True)
    content = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return '%s'%(self.introduction)
'''
class questionResponsesChutiya(models.Model):
    responseId = models.AutoField(primary_key = True)
    quiz = models.ForeignKey(quizResponses)
    #option = models.ForeignKey(optionsC, null = True, blank = True)
    question = models.ForeignKey(questions, null = True, blank = True)
    integerAnswer = models.CharField(max_length = 20,null = True, blank = True)
    def __unicode__(self):
        return '%s'%(self.quiz.quiz.name)
'''

class chutiyapa(models.Model):
    responseId = models.AutoField(primary_key = True)
    quiz = models.ForeignKey(quizResponses)
    fieldChutiyap = models.CharField(max_length = 10, null = True, blank = True)
    question = models.ForeignKey(questions, null = True, blank = True)
    def __unicode__(self):
        return '%s %s'%(self.quiz.quiz.name,self.question.question)

class Notifications(models.Model):
    token = models.TextField()
    def __unicode__(self):
        return self.token


class sheetpayment(models.Model):    
    tech = models.ForeignKey(TechProfile, null = True, blank = True)
    email = models.EmailField(max_length = 50, null = True, blank = True)
    status = models.CharField(max_length = 15,null= True,blank = True)
    ticketId = models.CharField(max_length = 100)
    contact = models.CharField(max_length = 20,null = True,blank = True)
    ticketPrice = models.IntegerField(null = True,blank = True)
    timeStamp = models.CharField(max_length = 50,null = True,blank = True)
    ticketName = models.CharField(max_length = 200,null = True,blank = True)
    def __unicode__(self):
        return self.email
        

class suggestions(models.Model):
    tech = models.ForeignKey(TechProfile , null = True , blank =True)
    suggestion = models.TextField(blank = True)
    def __unicode__(self):
        return self.tech.user.first_name

