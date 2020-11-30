from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from Tools.strTime import getChineseLocalStrTime

from userCenter.createUser import create_user,login,checkLoginStatus,logOut
from userCenter.userInfo import getUserInfo
from userCenter.setUser import setPassword,setTel,setEmail

def userCenterPage(request):
    if not request.is_ajax():
        headers = ["个人信息","运动记录","健康管理","运动计划","体质评测"]
        date,_ = getChineseLocalStrTime()
        args = {
            "title":"用户中心",
            "headers":headers,
            "date":date,
        }
        try:
            return render(request,"user/userCenter.html",args)
        except:
            return HttpResponse("404:无法加载网页")
    else:
        try:
            re = request.GET.get("re")
        except:
            return JsonResponse({"status": "error", "info": "没有获取到re参数", "result": None})
        if re=="setImage":
            # 设置头像
            pass
        elif re=="setPassword":
            # 设置密码
            try:
                id = request.GET.get("id")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数id", "result": None})
            try:
                status = request.GET.get("status")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数status", "result": None})
            try:
                password = request.GET.get("password")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数status", "result": None})
            r = setPassword(id,status,password)
            return JsonResponse(r)
        elif re=="setTel":
            # 设置电话
            try:
                id = request.GET.get("id")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数id", "result": None})
            try:
                status = request.GET.get("status")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数status", "result": None})
            try:
                tel = request.GET.get("tel")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数tel", "result": None})
            r = setTel(id,status,tel)
            return JsonResponse(r)
        elif re=="setEmail":
            # 设置邮箱地址
            try:
                id = request.GET.get("id")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数id", "result": None})
            try:
                status = request.GET.get("status")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数status", "result": None})
            try:
                email = request.GET.get("email")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数email", "result": None})
            r = setEmail(id,status,email)
            return JsonResponse(r)
        elif re=="info":
            # 获取用户信息
            try:
                id = request.GET.get("id")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数id", "result": None})
            try:
                status = request.GET.get("status")
            except:
                return JsonResponse({"status": "error", "info": "无法获取参数status", "result": None})
            r = getUserInfo(id,status)
            return JsonResponse(r)
        return JsonResponse({"status":"error","info":"no such order","result":None})

def sigInandsigUp(request):
    if not request.is_ajax():
        args={
            "title":"用户登录",
        }
        try:
            # print(args)
            return render(request,"user/signInandsingUp.html",args)
        except:
            return HttpResponse("404:无法加载网页")
    else:
        try:
            re = request.GET.get("re")
        except:
            return JsonResponse({"status":"error","info":"无法获取参数","result":None})
        if re=="logIn":
            try:
                index = request.GET.get("index")
            except:
                return JsonResponse({"status": "failed", "info": "请输入用户名/电话/邮箱地址", "result": None})
            try:
                password = request.GET.get("password")
            except:
                return JsonResponse({"status": "failed", "info": "请输入密码", "result": None})
            r = login(index,password)
            return JsonResponse(r)
        elif re=="SigUp":
            try:
                name = request.GET.get("name")
                if name=="":
                    return JsonResponse({"status": "failed", "info": "请输入用户名", "result": None})
            except:
                return JsonResponse({"status": "failed", "info": "请输入用户名", "result": None})
            try:
                password = request.GET.get("password")
                if len(password)<=0:
                    return JsonResponse({"status": "failed", "info": "请输入密码", "result": None})
            except:
                return JsonResponse({"status": "failed", "info": "请输入密码", "result": None})
            try:
                index = request.GET.get("index")
                if len(index)<=0:
                    return JsonResponse({"status": "failed", "info": "请输入联系方式", "result": None})
            except:
                return JsonResponse({"status": "failed", "info": "请输入联系方式", "result": None})
            r = create_user(name,password,index)
            return JsonResponse(r)
        elif re=="checkLogStatus":
            try:
                id = request.GET.get("id")
            except:
                return JsonResponse({"status": "failed", "info": "缺失参数id", "result": None})
            try:
                status = request.GET.get('status')
            except:
                return JsonResponse({"status": "failed", "info": "缺失参数status", "result": None})
            r = checkLoginStatus(id,status)
            return JsonResponse(r)
        elif re=="logOut":
            try:
                id = request.GET.get("id")
            except:
                return JsonResponse({"status": "failed", "info": "缺失参数id", "result": None})
            r = logOut(id)
            return JsonResponse(r)
        return JsonResponse({"status":"error","info":"no such order","result":None})

def log_Out(request):
    args = {
        "title":"退出登录",
    }
    return render(request,"user/logOut.html",args)