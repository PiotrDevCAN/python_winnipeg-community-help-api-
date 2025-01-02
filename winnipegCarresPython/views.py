from django.http import HttpResponse
from django.shortcuts import render
from .models import Community, Volunteer, User, HelpOffer, HelpType, HelpCategory 

def index(request):
    return HttpResponse("Hello, world. You're at the Winnipeg Carres REST API index.")

def community_list(request):
    return HttpResponse(f"Communities list")

def community_details(request, community_id):
    return HttpResponse(f"Details of community {community_id}")

def request_list(request):
    return HttpResponse(f"Requests list")

def request_details(request, community_id):
    return HttpResponse(f"Details of request {community_id}")

def offer_list(request):
    return HttpResponse(f"Offers list")

def offer_details(request, community_id):
    return HttpResponse(f"Details of offer {community_id}")

def help_type_list(request):
    return HttpResponse(f"Help types list")

def help_type_details(request, community_id):
    return HttpResponse(f"Details of help type {community_id}")

def help_category_list(request):
    return HttpResponse(f"Help categories list")

def help_category_details(request, community_id):
    return HttpResponse(f"Details of help category {community_id}")

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})

def volunteer_details(request, community_id):
    return HttpResponse(f"Details of volunteer {community_id}")