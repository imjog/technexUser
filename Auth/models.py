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
    def __unicode__(self):
        return self.collegeName
class FbConnect(models.Model):
    uid = models.CharField(max_length = 200, null = True)
    accessToken = models.CharField(max_length = 250, null = True)
    profileImage = models.TextField(validators=[URLValidator()],blank=True,null = True)

class TechProfile(models.Model):
    user = models.OneToOneField(User)
    year = models.IntegerField(choices=year_choices)
    mobileNumber = models.BigIntegerField()
    college = models.ForeignKey(College,null = True)
    fb = models.OneToOneField(FbConnect,null = True, blank = True)
    #profile_photo = models.TextField(validators=[URLValidator()],blank=True)

    def __unicode__(self):
        return "%s -%s" %(self.user.first_name, self.college)

class ParentEvent(models.Model):
    parentEventId = models.AutoField(primary_key = True)
    categoryName = models.CharField(max_length = 50)
    description = RichTextField(null = True,blank = True)
    order = models.SmallIntegerField(null = True, blank = True)
    nameSlug = models.SlugField(null = True)
    def __unicode__(self):
        return self.categoryName
    
class Event(models.Model):
    eventId = models.AutoField(primary_key = True)
    eventOrder = models.SmallIntegerField(null = True, blank = True)
    eventName = models.CharField(max_length = 50)
    parentEvent = models.ForeignKey(ParentEvent)
    description = RichTextField(null = True,blank = True)
    deadLine = models.DateTimeField(null = True,blank = True)
    prizeMoney = models.IntegerField(null=True, blank=True)
    maxMembers = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.eventName


class Team(models.Model):
    teamName = models.CharField(max_length=50, null=True, blank=True)
    teamId = models.AutoField(primary_key = True)
    event = models.ForeignKey(Event)
    teamLeader = models.ForeignKey(TechProfile,related_name = 'teamLeader')
    members = models.ManyToManyField(TechProfile,related_name = 'members')

    def __unicode__(self):
        return self.teamName

class EventOption(models.Model):
    optionName = models.CharField(max_length = 50, null = True)
    optionDescription = RichTextField()
    eventOptionOrder = models.SmallIntegerField(null = True, blank = True)
    event = models.ForeignKey(Event)
    def __unicode__(self):
        return '%s %s'%(self.optionName,self.event)


