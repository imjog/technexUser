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
	prepopulated_fields = {'nameSlug':('eventName',)}
class parentEventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'nameSlug': ('categoryName',)}
    
admin.site.register(TechProfile)
admin.site.register(College)
#admin.site.register(Event,EventAdmin)
admin.site.register(ParentEvent, parentEventAdmin)
admin.site.register(Team)
admin.site.register(EventOption)
admin.site.register(FbConnect)
admin.site.register(ForgotPass)
admin.site.register(GuestLecture)
admin.site.register(Workshops)
admin.site.register(WorkshopOptions)
admin.site.register(WorkshopTeam)