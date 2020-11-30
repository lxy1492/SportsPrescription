from django.urls import path,include
from django.conf.urls import url
from userCenter.userViews import userCenterPage
from userCenter.userViews import sigInandsigUp
from userCenter.userViews import log_Out

urlpatterns = [
    url("^$",userCenterPage),
    url("^sigIn/$",sigInandsigUp),
    url("^logOut/$",log_Out),
]