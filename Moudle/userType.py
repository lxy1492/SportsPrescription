import os,pickle,time,random
from uuid import uuid4,uuid1
from Moudle.sportMoudle import effect,target
from Moudle.courseMoudle import Course
from SportsPrescription.config import user as config

BaseDIR = config["DIR"]
ImageDIR = config["ImageDIR"]
AccountDIR = config["AccountDIR"]

class User():
    def __init__(self,name=None,password=None,id=None,sex=None,tel=None,email=None,image=None,target=None,effect=None):
        self.name = name
        self.password = password
        self.id = id
        self.sex = sex
        self.tel = tel
        self.email = email
        self.image = image
        self.target = target
        self.effect  =effect
        self.history = None
        self.lastTime = None
        self.currentCourse = None
        self.loginStatus = False
        self.identifyCode = None
        self.lastLocation = None
        self.temp = {}

    @ property
    def Dict(self):
        d = {
            "name":self.name,
            "id":self.id,
            "sex":self.sex,
            "tel":self.tel,
            "email":self.email,
            "image":self.image,
            "target":self.target,
            "effect":self.effect,
            "history":self.history,
            "loginStatus":self.loginStatus,
            "identifyCode":self.identifyCode,
        }
        return d

    def setSex(self,sex):
        if isinstance(sex,str):
            if sex in ["man","madam"]:
                self.sex = sex
        elif sex == None:
            self.sex=sex

    def setID(self,id:str=None):
        if not isinstance(id,str) or id==None:
            id = uuid4()
        if isinstance(id,str):
            self.id = id
            return id
        else:
            return None

    def setTel(self,tel,save=True):
        if isinstance(tel,str):
            if len(tel)==11:
                try:
                    _ = int(tel)
                    self.tel = tel
                    if save:
                        self.save()
                    return self.tel
                except:
                    return -1
        elif isinstance(tel,int):
            tel = str(tel)
            return self.setTel(tel)
        return None

    def setEmail(self,address,save=True):
        if isinstance(address,str):
            if "@" in address and "." in address:
                self.email = address
                if save:
                    self.save()
                return 0
        return -1


    def setImage(self,href):
        if isinstance(href):
            if "http://" in href:
                self.image = href
            else:
                if os.path.exists(href):
                    self.image = href

    def setEffect(self,e):
        if isinstance(e,str):
            if e in effect:
                if isinstance(self.effect,list):
                    self.effect.append(e)
                else:
                    self.effect = [e]
        elif isinstance(e,list):
            for each in e:
                self.setEffect(each)

    def setTarget(self,t):
        if isinstance(t,str):
            if t in target:
                if isinstance(self.target,list):
                    self.target.append(t)
                else:
                    self.target = [t]
        elif isinstance(t,list):
            for each in t:
                self.setTarget(each)

    def setLastTime(self):
        self.lastTime = time.time()

    def setCurrentCourse(self,course):
        if isinstance(course,Course):
            if isinstance(self.currentCourse,list):
                self.currentCourse.append(course)
            else:
                self.currentCourse = [course]
        elif isinstance(course,list):
            for each in course:
                self.setCurrentCourse(each)

    def getAllAccounts(self,dir = AccountDIR):
        accounts = []
        for each in os.listdir(dir):
            if isinstance(each,str):
                if each.split(".")[-1] == "tbs":
                    accounts.append(each.split(".tbs")[0])

    def setID(self,id):
        accounts = self.getAllAccounts()
        if isinstance(id,str):
            if not id in accounts:
                return -1
            else:
                self.id = id

    def save(self):
        if not os.path.exists(BaseDIR):
            os.makedirs(BaseDIR)
        if not os.path.exists(AccountDIR):
            os.makedirs(AccountDIR)
        if self.id==None:
            return -1
        if isinstance(self.id,str):
            fileName = self.id+".tbs"
            path = AccountDIR+fileName
            if os.path.exists(path):
                with open(path,"wb") as f:
                    f.write(pickle.dumps(self))
                return 0
            else:
                with open(path,"wb") as f:
                    f.write(pickle.dumps(self))
                return 1

    def getloginStatusUID(self):
        uln = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        num = 22
        rs = random.sample(uln,num)
        id = uuid1()
        return "".join(rs+str(id).split("-"))

    def login(self,id=None,saveself=False):
        if id==None or not isinstance(id,str):
            id = self.getloginStatusUID()
        self.loginStatus = id
        if saveself:
            self.save()
        return self.loginStatus

    def setPassword(self,pwd,save=True):
        if isinstance(pwd,str):
            if pwd!="":
                self.password = pwd
                if save:
                    self.save()
                return self.password
        return None

if __name__ == '__main__':
    app = User()