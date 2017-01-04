from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.core.validators import URLValidator
year_choices = [
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
    ]

def get_user_image_folder(instance, filename):
    return "technexusers/%s-%s/%s" %(instance.user.first_name,instance.user.last_name, filename)


class College(models.Model):
    collegeId = models.AutoField(primary_key = True)
    collegeName = models.CharField(max_length=250)
    status = models.BooleanField(default = False)
    def __unicode__(self):
        return self.collegeName
class FbConnect(models.Model):
    uid = models.CharField(max_length = 200, null = True)
    accessToken = models.CharField(max_length = 250, null = True)
    profileImage = models.TextField(validators=[URLValidator()],blank=True,null = True)
    def __unicode__(self):
        return self.uid
class TechProfile(models.Model):
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
    #profile_photo = models.TextField(validators=[URLValidator()],blank=True)

    def __unicode__(self):
        return "%s -%s" %(self.user.first_name, self.college)

class ParentEvent(models.Model):
    parentEventId = models.AutoField(primary_key = True)
    categoryName = models.CharField(max_length = 50)
    description = RichTextField(null = True,blank = True)
    order = models.SmallIntegerField(default = 0)
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
    def __unicode__(self):
        return self.eventName


class Team(models.Model):
    teamName = models.CharField(max_length=50, null=True, blank=True)
    teamId = models.AutoField(primary_key = True)
    technexTeamId = models.CharField(max_length = 10, null = True, blank = True)
    event = models.ForeignKey(Event)
    teamLeader = models.ForeignKey(TechProfile,related_name = 'teamLeader')
    members = models.ManyToManyField(TechProfile,related_name = 'members',null = True)

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
    description = RichTextField()
    time = models.DateTimeField(auto_now = True)
    photo = models.TextField(validators=[URLValidator()],blank=True)

class ReaderStatus(models.Model):
    reader = models.ForeignKey(TechProfile)
    notification = models.ForeignKey(Notification)
    status = models.BooleanField(default = True)

class StartUpFair(models.Model):
    idea = models.CharField(max_length = 250)
    teamLeader = models.OneToOneField(TechProfile)
    teamName = models.CharField(max_length = 35)
    def __unicode__(self):
        return self.teamName

class StartUpMails(models.Model):
    email = models.EmailField(max_length = 65,unique = True)
    team = models.ForeignKey(StartUpFair)
    def __unicode__(self):
        return self.email        