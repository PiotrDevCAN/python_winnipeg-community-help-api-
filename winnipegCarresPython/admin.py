from django.contrib import admin
from .models import Community, User, Volunteer, Offer, Request, HelpType, HelpCategory

admin.site.register(Community)
admin.site.register(User)
admin.site.register(Volunteer)
admin.site.register(Offer)
admin.site.register(Request)
admin.site.register(HelpType)
admin.site.register(HelpCategory)
