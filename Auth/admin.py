from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from Auth.models import *

class eventOptionInline(admin.TabularInline):
	model = EventOption
	extra = 1

@admin.register(Event)	
class EventAdmin(admin.ModelAdmin):
	inlines = [eventOptionInline]
admin.site.register(TechProfile)
admin.site.register(College)
#admin.site.register(Event,EventAdmin)
admin.site.register(ParentEvent)
admin.site.register(Team)
admin.site.register(EventOption)