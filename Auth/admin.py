from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from Auth.models import *

admin.site.register(TechProfile)
admin.site.register(College)
admin.site.register(Event)
admin.site.register(ParentEvent)
admin.site.register(Team)
