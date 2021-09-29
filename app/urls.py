from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('enter',views.enter, name='enter'),
    path('judging',views.judging, name='judging'),
    path('media',views.media, name='media'),
    path('contact',views.contact, name='contact'),
    path('awards',views.awards, name='awards'),
    path('vote',views.vote, name='vote'),
]
