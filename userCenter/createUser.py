from user import manage
from Moudle.userType import User

def create_user(name,password,index):
    d = {
        "status":"success",
        "info":"创建成功",
        "result":None
    }
    u = manage.createUser(name,password,index)
    if isinstance(u,User):
        d["result"]={
            "id":u.id,
            "statusCode":u.loginStatus
        }
    else:
        if isinstance(u,int) or isinstance(u,float):
            if u==-1:
                d["status"]="failed"
                d["info"]="此用户名已存在"
            elif u==-2 or u==-3:
                d["status"] = "failed"
                d["info"] = "电话号码或邮件地址格式错误"
            elif u==-4:
                d["status"] = "failed"
                d["info"] = "该电话号码已存在"
            elif u==-5:
                d["status"] = "failed"
                d["info"] = "邮件地址格式错误"
            elif u==-6:
                d["status"] = "failed"
                d["info"] = "该邮件地址已存在"
        else:
            d["status"]="error"
            d["info"]="未注册成功"
    return d

def login(index,password):
    u = manage.loadAccount(index)
    if isinstance(u,User):
        if u.password == password:
            statusCode = u.login(saveself=True)
            id = u.id
            # u.save()
            return {
                "status":"success",
                'info':"登录成功",
                "result":{
                    "status":statusCode,
                    "id":id,
                }
            }
        else:
            return {
                "status": "failed",
                'info': "密码错误",
                "result": {
                    "status": None,
                    "id": None,
                }
            }
    return {
        "status": "error",
        'info': "不存在此用户",
        "result": {
            "status": None,
            "id": None,
        }
    }

def checkLoginStatus(id,status):
    u = manage.loadAccountByID(id)
    if u!=None:
        if isinstance(u,User):
            if u.loginStatus==status:
                return {
                    "status":"success",
                    "info":"已登录",
                    "result":None
                }
    return {
        "status":"failed",
        'info':"未登录",
        "result":None,
    }

def logOut(id):
    u = manage.loadAccountByID(id)
    if isinstance(u,User):
        u.loginStatus = None
        u.save()
    return {
        "status":"success",
        "info":"退出登录",
        "result":None,
    }