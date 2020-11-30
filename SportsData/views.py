import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from SportsData.getData import getRandomData

def sportsLineData(request):
    if request.is_ajax():
        re  = request.GET.get("re")
        if re=="random":
            start = request.GET.get("start")
            length = request.GET.get("length")
            start = int(start)
            data = getRandomData(returnDICT=True)
            num = len(data)
            try:
                length = int(length)
            except:
                length = None
            if length!=None:
                end = start+length
            else:
                end = num
            if start>=num:
                return JsonResponse({"status": "failed", "info": "超出范围，起始点："+str(start)+"，数据量："+str(length), "data": None})
            else:
                if end >= num-1:
                    end = num-1
                return JsonResponse({"status":"success","info":"获取成功","data":data[start:end]})
        else:
            return JsonResponse({"status": "error", "info": "没有这个指令", "data": None})
    return render(request,"SportsData/line.html")

def runningData(request,*args):
    # print(args)
    start = args[0]
    length = args[1]
    start = int(start)
    data = getRandomData(returnDICT=True)
    num = len(data)
    try:
        length = int(length)
    except:
        length = None
    if length != None:
        end = start + length
    else:
        end = num
    if start >= num:
        # return HttpResponse(json.dumps({"status": "failed", "info": "超出范围，起始点：" + str(start) + "，数据量：" + str(length), "data": None}))
        return JsonResponse(
            {"status": "failed", "info": "超出范围，起始点：" + str(start) + "，数据量：" + str(length), "data": None})
    else:
        if end >= num - 1:
            end = num - 1
        # return HttpResponse(json.dumps({"status": "success", "info": "获取成功", "data": data[start:end]}))
        return JsonResponse({"status": "success", "info": "获取成功", "data": data[start:end]})
