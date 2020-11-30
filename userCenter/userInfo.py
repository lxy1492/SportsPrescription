from Moudle.userType import User
from user import manage

def getUserInfo(id,status):
    u = manage.loadAccountByID(id)
    if isinstance(u,User):
        if u.loginStatus!=status:
            return {
                "status":"failed",
                "info":"未登录",
                "result":None,
            }
        d = u.Dict
        try:
            d.pop("password")
        except:
            pass
        return {
            "status":"success",
            "info":'获取成功',
            "result":d,
        }
    return {
        "status":"failed",
        "info":"获取失败",
        "result":None,
    }

