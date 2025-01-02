from django.contrib import admin
from .models import Community, User, Volunteer, HelpOffer, HelpType, HelpCategory

admin.site.register(Community)
admin.site.register(User)
admin.site.register(Volunteer)
admin.site.register(HelpOffer)
admin.site.register(HelpType)
admin.site.register(HelpCategory)
