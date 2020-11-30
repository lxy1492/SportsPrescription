from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from Prescription import views

url = [
    url("sportsList.html/$",views.sportsList),
    url("coursesList.html/$",views.coursesList),
    url("addSport.html/$",views.addSport),
    url("addCourse.html/$",views.addCourse),
    url("^$",views.index),
]