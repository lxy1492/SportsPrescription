from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from Moudle.sportMoudle import Sport
from Moudle.courseMoudle import Course
from Moudle.sportMoudle import target,effect
from Prescription.manage import getSport,getCourse
from SportsPrescription.config import prescription as prescriptionConfigure

def index(request):
    title = "运动处方"
    return render(request,"Prescription/index.html",{"title":title})

def sportsList(request):
    if request.is_ajax():
        try:
            re = request.GET.get("re")
        except:
            re = None
        if re!=None:
            if re == "getsport":
                try:
                    name = request.GET.get("name")
                    # print(name)
                    if isinstance(name,str):
                        data = getSport.loadSport(name)
                        if data==None:
                            return JsonResponse({"status": "error", "result": None, "info": "无法加载运动："+name})
                        else:
                            if isinstance(data,dict):
                                return JsonResponse({"status":"success","result":data,"info":"获取到运动："+name})
                            elif isinstance(data,Sport):
                                return JsonResponse({"status": "success", "result": data.Dict, "info": "获取到运动：" + name})
                            else:
                                return JsonResponse({"status": "error", "result": None, "info": "无法获取运动数据：" + name})
                    return JsonResponse({"status": "error", "result": None, "info": "name参数错误"})
                except:
                    return JsonResponse({"status": "error", "result": None, "info": "没有获取到参数：name"})
            elif re=="setEffect":
                try:
                    name = request.GET.get("name")
                except:
                    return JsonResponse({'statu':'error',"info":"无法获取参数：name","result":None})
                try:
                    e = request.GET.get("target")
                except:
                    return JsonResponse({'statu':'error',"info":"无法获取参数：target","result":None})
                try:
                    type_ = request.GET.get("type")
                    if isinstance(type_, str):
                        if type_.lower() == "true":
                            type_ = True
                        else:
                            type_ = False
                except:
                    return JsonResponse({'statu': 'error', "info": "无法获取参数：type", "result": None})
                r = getSport.setEffect(name,type_,e)
                if r!=None:
                    return JsonResponse({"status":"success","result":r,"info":"设置成功"})
                else:
                    return JsonResponse({"status":"failed","result":None,"info":"设置失败"})
            elif re=="setTarget":
                try:
                    name = request.GET.get("name")
                except:
                    return JsonResponse({'statu': 'error', "info": "无法获取参数：name", "result": None})
                try:
                    e = request.GET.get("target")
                except:
                    return JsonResponse({'statu': 'error', "info": "无法获取参数：target", "result": None})
                try:
                    type_ = request.GET.get("type")
                    if isinstance(type_,str):
                        if type_.lower()=="true":
                            type_=True
                        else:
                            type_ = False
                except:
                    return JsonResponse({'statu': 'error', "info": "无法获取参数：type", "result": None})
                r = getSport.setTarget(name, type_, e)
                if r != None:
                    return JsonResponse({"status": "success", "result": r, "info": "设置成功"})
                else:
                    return JsonResponse({"status": "failed", "result": None, "info": "设置失败"})
            elif re=="rename":
                try:
                    newname = request.GET.get("newname")
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：newname", "result": None})
                try:
                    oldname = request.GET.get("oldname")
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：oldname", "result": None})
                if isinstance(newname,str) and isinstance(oldname,str):
                    if newname!="" and oldname!="":
                        try:
                            s = getSport.loadSport(oldname,returnDict=False)
                            s.name = newname
                            s.save()
                            return JsonResponse({'status': 'success', "info": "设置成功", "result": s.Dict})
                        except:
                            return JsonResponse({'status': 'error', "info": "无法加载运动项目:"+oldname, "result": None})
                    else:
                        return JsonResponse({'status': 'error', "info": "参数oldname为空或newname为空", "result": None})
                else:
                    return JsonResponse({'status': 'error', "info": "参数oldname数据类型错误或newname数据类型错误", "result": None})
            elif re=="setSportTime":
                try:
                    sport = request.GET.get("sport")
                    if not isinstance(sport,str):
                        return JsonResponse({'status': 'error', "info": "sport参数类型错误："+sport, "result": None})
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：sport", "result": None})
                try:
                    time_ = request.GET.get("time")
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：time", "result": None})
                if isinstance(time_,str):
                    try:
                        time_=float(time_)
                    except:
                        return JsonResponse({'status': 'error', "info": "无法将字符类型参数time转化成float类型："+time_, "result": None})
                elif isinstance(time_,int):
                    time_ = float(time_)
                if isinstance(time_,float):
                    try:
                        s = getSport.loadSport(sport,returnDict=False)
                    except:
                        return JsonResponse({'status': 'error', "info": "无法加载运动："+sport, "result": None})
                    if isinstance(s,Sport):
                        s.setSportsTime(time_)
                        s.save()
                        return JsonResponse({'status': 'success', "info": "设置成功", "result":s.Dict})
                    else:
                        return JsonResponse({'status': 'error', "info": "无法加载运动："+sport, "result": None})
                else:
                    return JsonResponse({'status': 'error', "info": "无法处理参数time", "result": None})
            elif re=="setStrength":
                try:
                    sport = request.GET.get("sport")
                    if not isinstance(sport, str):
                        return JsonResponse({'status': 'error', "info": "sport参数类型错误：" + sport, "result": None})
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：sport", "result": None})
                try:
                    strength = request.GET.get("strength")
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：strength", "result": None})
                if isinstance(strength,str):
                    try:
                        strength = float(strength)
                    except:
                        return JsonResponse({'status': 'error', "info": "无法将字符类型strength参数转化为浮点类型", "result": None})
                elif isinstance(strength,int):
                    strength = float(strength)
                if isinstance(strength,float):
                    s = getSport.loadSport(sport,returnDict=False)
                    if isinstance(s,Sport):
                        r = s.setStrength(strength)
                        if r>=0:
                            s.save()
                            return JsonResponse({'status': 'success', "info": "设置成功", "result": s.Dict})
                        else:
                            return JsonResponse({'status': 'failed', "info": "设置失败", "result": None})
                    else:
                        return JsonResponse({'status': 'error', "info": "加载失败："+sport, "result": None})
                else:
                    return JsonResponse({'status': 'error', "info": "参数类型错误：strength", "result": None})
            elif re=="setFrequency":
                try:
                    sport = request.GET.get("sport")
                    if not isinstance(sport, str):
                        return JsonResponse({'status': 'error', "info": "sport参数类型错误：" + sport, "result": None})
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：sport", "result": None})
                try:
                    frequency = request.GET.get("frequency")
                except:
                    return JsonResponse({'status': 'error', "info": "无法获取参数：frequency", "result": None})
                if isinstance(frequency,str):
                    try:
                        frequency = float(frequency)
                    except:
                        return JsonResponse({'status': 'error', "info": "转换字符类型参数frequency错误", "result": None})
                elif isinstance(frequency,int):
                    frequency = float(frequency)
                if isinstance(frequency,float):
                    s = getSport.loadSport(sport,returnDict=False)
                    if isinstance(s,Sport):
                        r = s.setFrequency(frequency)
                        if r>=0:
                            s.save()
                            return JsonResponse({'status': 'success', "info": "设置成功", "result": s.Dict})
                        else:
                            return JsonResponse({'status': 'failed', "info": "设置失败", "result": None})
                    else:
                        return JsonResponse({'status': 'error', "info": "无法加载运动:"+sport, "result": None})
                else:
                    return JsonResponse({'status': 'error', "info": "无法处理参数：frequency", "result": None})
            return JsonResponse({"status":"error","result":None,"info":"无法处理请求:"+re})

        return JsonResponse({"status":"error","result":None,"info":"无法处理请求"})
    else:
        l = getSport.get_sport_list()
        title = "运动项目"
        l = [s[0].split(".")[0] for s in l]
        return render(request,"Prescription/sportsList.html",{"title":title,"sports":l,"target":target,"effect":effect})

def coursesList(request):
    if request.is_ajax():
        re = request.GET.get("re")
        if re == "getCoursesList":
            try:
                name = request.GET.get("name")
            except:
                return JsonResponse({"status":"error","info":"获取不到参数name","result":None})
            data = getCourse.loadCourse(name)
            return JsonResponse({"status":"success","info":"获取到"+name,"result":data})
        else:
            return JsonResponse({"status":"error","info":"无法处理指令:"+re,"result":None})
    else:
        l = getCourse.getCourseList()
        if l==None:
            l = []
        return render(request,"Prescription/coursesList.html",{"title":"运动处方","courses":l,"target":target,"effect":effect})

def addSport(request):
    if request.is_ajax():
        re = request.GET.get("re")
        if re=="addSport":
            try:
                name = request.GET.get("name")
            except:
                return JsonResponse({"status":"error","info":"没有获取到参数:name","result":None})
            try:
                belong = request.GET.get('belong')
            except:
                belong = []

        return JsonResponse({"status":"error","info":"没有相关指令","result":None})
    else:
        cl = getCourse.getCourseList()
        title = "创建运动项目"
        args = {"title":title,"courseList":cl,"target":target,"effect":effect}
        return render(request,"Prescription/addSport.html",args)

def addCourse(request):
    if request.is_ajax():
        re = request.GET.get("re")
        if re=="create":
            try:
                name = request.GET.get("name")
            except:
                return JsonResponse({"status": "error", "info": "没有获取到参数:name", "result": None})
            try:
                difficulty = request.GET.get("difficulty")
            except:
                return JsonResponse({"status": "error", "info": "没有获取到参数:difficulty", "result": None})
            try:
                description = request.GET.get("description")
            except:
                description = None
            try:
                type_ = request.GET.get("type")
            except:
                return JsonResponse({"status": "error", "info": "没有获取到参数:type", "result": None})
            try:
                pioneer = request.GET.get("pioneer")
            except:
                pioneer = None
            c = Course(name=name,difficulty=int(difficulty),description=description,pioneer=pioneer)
            c.setSaveDIR(prescriptionConfigure["courseDIR"])
            c.save()
            return ({"status":"success","info":"创建"+name+"成功","result":c.Dict})
        return JsonResponse({"status":"error","info":"没有相关指令","result":None})
    else:
        args = {
            "title":"创建处方",
        }
        return render(request,"Prescription/addCourse.html",args)