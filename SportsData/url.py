from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from SportsData import views

url = [
    url(r"line.html",views.sportsLineData),
    url(r"^data/start(\w+)length(.+)/$",views.runningData),
]