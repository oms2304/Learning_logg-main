"""Defines URL patterns for learning_logs."""
 #import url function needed for mapping URLs to views
 #Django needs to figure out which view function should handle that request, and it uses urls.py to make that decision.

from .import views 
from django.urls import path #import the views module (the . tells python to import views from the same directory as the current urls.py module)

app_name = 'learning_logs'

urlpatterns = [ # a list of indiividual pages that can be requested from the learning_logs app.     
    #Home page
    path('', views.index, name='index'),

    #show all topics
    path('topics/', views.topics, name='topics'),

    #Details for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'), #int:topic_id assigns an integer to argument topic_id, django puts it in Topic(topic_id)

    path('new_topic/', views.new_topic, name='new_topic'),

    path('new_entry/<int:topic_id>/', views.new_entry, name ='new_entry'), #puts the topic_id into the url so it can be grabbed later by views
                        
    path('edit_entry/<int:entry_id>/', views.edit_entry, name ='edit_entry'),
]