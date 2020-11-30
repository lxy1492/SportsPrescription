from Moudle.userType import User
from user import manage

def setEmail(userID,status,email):
    if manage.emailExists(email):
        return {
            "status":"failed",
            "info":"已存在此邮箱地址",
            "result":None
        }
    u = manage.loadAccountByID(userID)
    if isinstance(u,User):
        if u.loginStatus==status:
            r = u.setEmail(email)
            if r>=0:
                manage.changeEmailForUserTable(email,userID)
                return {
                    "status":"success",
                    "info":"设置成功",
                    "result":u.email,
                }
            else:
                return {
                    "status": "failed",
                    "info": "格式错误",
                    "result": None,
                }
        else:
            return {
                "status": "failed",
                "info": "未登录",
                "result": None,
            }
    else:
        return {
            "status": "error",
            "info": "无法获取账户",
            "result": None,
        }

def setTel(userID,status,tel):
    if manage.telExists(tel):
        return {
            "status":"failed",
            "info":"已存在此电话号码",
            "result":None,
        }
    u = manage.loadAccountByID(userID)
    if isinstance(u,User):
        if u.loginStatus==status:
            r = u.setTel(tel)
            if r==-1:
                return {
                    "status": "error",
                    "info": "无法将"+str(tel)+"设置为用户电话",
                    "result": None,
                }
            elif u==None:
                return {
                    "status": "error",
                    "info": "遇到未知错误",
                    "result": None,
                }
            else:
                manage.changeTelForUserTable(tel,userID)
                return {
                    "status": "success",
                    "info": "设置成功",
                    "result": u.tel,
                }
        else:
            return {
                "status": "failed",
                "info": "未登录",
                "result": None,
            }
    else:
        return {
            "status": "error",
            "info": "无法获取账户",
            "result": None,
        }

def setPassword(id,status,new):
    u = manage.loadAccountByID(id)
    if isinstance(u,User):
        if u.loginStatus!=status:
            return {
                "status": "failed",
                "info": "未登录",
                "result": None,
            }
        else:
            if u.password==new:
                return {
                    "status":"failed",
                    "info":"密码为更改",
                    "result":None,
                }
            else:
                u.setPassword(new)
                return {
                    "status":"success",
                    "info":"设置成功",
                    "result":u.password,
                }
    else:
        return {
            "status": "error",
            "info": "无法获取账户",
            "result": None,
        }
