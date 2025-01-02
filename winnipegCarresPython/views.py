from django.http import HttpResponse
from django.shortcuts import render
from .models import Community, Volunteer, User, HelpType, HelpCategory, Offer, Request
from .forms import VolunteerForm


def index(request):
    return HttpResponse("Hello, world. You're at the Winnipeg Carres REST API index.")

def community_list(request):
    communities = Community.objects.all()
    return render(request, 'community_list.html', {'communities': communities})

def community_details(request, community_id):
    return HttpResponse(f"Details of community {community_id}")


def request_list(request):
    requests = Request.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

def request_details(request, community_id):
    return HttpResponse(f"Details of request {community_id}")


def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'offer_list.html', {'offers': offers})

def offer_details(request, community_id):
    return HttpResponse(f"Details of offer {community_id}")


def request_list(request):
    requests = Request.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

def request_details(request, community_id):
    return HttpResponse(f"Details of request {community_id}")


def help_type_list(request):
    helpTypes = HelpType.objects.all()
    return render(request, 'help_type_list.html', {'helpTypes': helpTypes})

def help_type_details(request, community_id):
    return HttpResponse(f"Details of help type {community_id}")


def help_category_list(request):
    helpCategories = HelpCategory.objects.all()
    return render(request, 'help_category_list.html', {'helpCategories': helpCategories})

def help_category_details(request, community_id):
    return HttpResponse(f"Details of help category {community_id}")


def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})

def volunteer_details(request, community_id):
    return HttpResponse(f"Details of volunteer {community_id}")

def volunteer_registration(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            # Process the form data
            print(form.cleaned_data)  # For debugging purposes
            return render(request, 'success.html', {'form': form})
    else:
        form = VolunteerForm()

    return render(request, 'volunteer_registration.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_details(request, community_id):
    return HttpResponse(f"Details of user {community_id}")