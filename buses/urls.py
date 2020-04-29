from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view),
    path('search/', views.search_view),
    path('ajax/stoppage/', views.ajax_stoppage),
    path('ajax/search/', views.ajax_search),
    path('buses/', views.buslist_view),
    path('bus/<int:pk>', views.busdetail_view),
    path('about/', views.about_view),
]