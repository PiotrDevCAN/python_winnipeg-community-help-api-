"""
URL configuration for winnipegCarresPython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),

    path('api/community/list/', views.community_list, name='community_list'),
    path('api/community/<int:community_id>/', views.community_details, name='community_details'),  # Dynamic URL with community_id

    path('api/request/list/', views.request_list, name='request_list'),
    path('api/request/<int:community_id>/', views.request_details, name='request_details'),  # Dynamic URL with community_id

    path('api/offer/list/', views.offer_list, name='offer_list'),
    path('api/offer/<int:community_id>/', views.offer_details, name='offer_details'),  # Dynamic URL with community_id

    path('api/help-type/list/', views.help_type_list, name='help_type_list'),
    path('api/help-type/<int:community_id>/', views.help_type_details, name='help_type_details'),  # Dynamic URL with community_id

    path('api/help-category/list/', views.help_category_list, name='help_category_list'),
    path('api/help-category/<int:community_id>/', views.help_category_details, name='help_category_details'),  # Dynamic URL with community_id

    path('api/volunteer/list/', views.volunteer_list, name='volunteer_list'),
    path('api/volunteer/<int:community_id>/', views.volunteer_details, name='volunteer_details'),  # Dynamic URL with community_id

    path('api/user/list/', views.user_list, name='user_list'),
    path('api/user/<int:community_id>/', views.user_details, name='user_details'),  # Dynamic URL with community_id
]
