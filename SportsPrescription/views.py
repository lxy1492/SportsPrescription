from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    menue = ["运动处方", "发现运动", "方案制定", "运动计划", "运动分享", "个人中心"]  # 此处必须是六个
    args = {
        'title':"运动处方",
        'header1_1':"运动",
        'header1_2':"处方",
        'header2':"寻找最适合你的运动方案  保障运动效力",
        "menue":menue,
    }
    return render(request,"home.html",args)


