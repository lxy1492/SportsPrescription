import os,random,json,pickle
from uuid import uuid4
from Moudle.userType import BaseDIR,AccountDIR,ImageDIR,User
# from SportsPrescription.config import user as config

userTablePath = BaseDIR+"userTable.tbs"

def loadUsertable(path=userTablePath):
    if os.path.exists(path):
        with open(path,"r") as f:
            try:
                table = json.loads(f.read())
                return table
            except:
                return None
    return None

def createUserTable(table=None,path=userTablePath):
    if table==None:
        table = {}
    if isinstance(table,dict):
        with open(path,"w") as f:
            f.write(json.dumps(table))
            return 0
    return -1

def getUID():
    table = loadUsertable()
    l = []
    if isinstance(table,dict):
        for each in table:
            l.append(each)
    return l

def addUserToTable(id,name=None,tel=None,email=None):
    table = loadUsertable()
    if isinstance(table,dict):
        d = {
            id:{
                "name":name,
                "tel":tel,
                "email":email,
            }
        }
        table.update(d)
    else:
        table = {
            id:{
                "name":name,
                "tel":tel,
                "email":email,
            }
        }
    # print(table)
    createUserTable(table)

def checkUserID(id):
    table = loadUsertable()
    if isinstance(table,dict):
        if id in table:
            return False
    return True

def nameExists(name:str,table=None):
    if not isinstance(name,str):
        return False
    if table==None:
        table = loadUsertable()
    if isinstance(table,dict):
        for each in table:
            if table[each]["name"]==name:
                return True
    return False

def telExists(tel,table=None):
    if isinstance(tel,int):
        tel = str(tel)
    if isinstance(tel,str):
        if table==None:
            table = loadUsertable()
        if isinstance(table,dict):
            for each in table:
                if table[each]["tel"] == tel:
                    return True
    return False

def emailExists(email,table=None):
    if isinstance(email,str):
        if table==None:
            table = loadUsertable()
        if isinstance(table,dict):
            for each in table:
                if table[each]["email"]==email:
                    return True
    return False

def removeFromUserTable(id):
    table = loadUsertable()
    if isinstance(table,dict):
        table.pop(id)
    createUserTable(table)

def createAccount(name:str,password:str,tel=None,email=None):
    '''

    :param name:用户名，必须
    :param password: 密码，必须
    :param tel: 电话号码，十一位数字
    :param email: 邮箱地址
    :return: -1代表失败，返回User代表成功
    '''
    dir = AccountDIR
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not isinstance(name,str):
        return -1
    if nameExists(name):
        return -1
    else:
        table = loadUsertable()
        if isinstance(tel,int):
            tel = str(tel)
        if isinstance(tel,str):
            if len(tel)!=11:
                return -2
            else:
                try:
                    _ = int(tel)
                except:
                    return -3
        if tel!=None:
            if telExists(tel,table):
                return -4
        if isinstance(email,str):
            if not "@" in email:
                return -5
        if email!=None:
            if emailExists(email,table):
                return -6
        u = User(name=name,password=password,tel=tel,email=email)
        userID = uuid4()
        userID = "".join(str(userID))
        if isinstance(table,dict):
            while(userID in table):
                userID = uuid4()
        u.id = userID
        addUserToTable(userID,u.name,u.tel,u.email)
        u.save()
        u.login()
        return u
    return -1

def loadAccount(index):
    '''

    :param index:可以是姓名，也可以是电话，或邮箱
    :return: 返回None或者User
    '''
    id = None
    table = loadUsertable()
    if isinstance(index,int):
        index = str(int)
    if len(index)==11:
        for each in table:
            if table[each]["tel"] == index:
                id = each
                break
    elif "@" in index:
        for each in table:
            if table[each]["email"] == index:
                id = each
                break
    else:
        for each in table:
            if table[each]["name"]==index:
                id = each
    if id==None:
        return id
    else:
        fileName = AccountDIR+id+".tbs"
        if os.path.exists(fileName):
            with open(fileName,"rb") as f:
                u = pickle.loads(f.read())
                return u
    return None

def removeUser(index):
    '''

    :param index:可以是姓名，也可以是电话或邮箱
    :return: 返回无意义
    '''
    id = None
    table = loadUsertable()
    if isinstance(index, int):
        index = str(int)
    if len(index) == 11:
        for each in table:
            if table[each]["tel"] == index:
                id = each
                break
    elif "@" in index:
        for each in table:
            if table[each]["email"] == index:
                id = each
                break
    else:
        for each in table:
            if table[each]["name"] == index:
                id = each
    if isinstance(id,str):
        fileName = AccountDIR+id+".tbs"
        if os.path.exists(fileName):
            os.remove(fileName)
        removeFromUserTable(id)


def AccountList():
    dir = AccountDIR
    if not os.path.exists(dir):
        os.makedirs(dir)
        return None
    l = []
    for each in os.listdir(dir):
        if ".tbs" in each:
            if each.split(".")[-1]=="tbs":
                l.append(each.split(".tbs")[0])
    if len(l)>0:
        return l
    else:
        return None

def deleteAccount(index):
    removeUser(index)

def loadUserFromFile(name):
    if not os.path.exists(name):
        if not ".tbs" in name:
            name = name+".tbs"
        name = AccountDIR+name
    if os.path.exists(name):
        with open(name,"rb") as f:
            u = pickle.loads(f.read())
            return u
    return None

def reflashTable():
    '''
    刷新usertable文件
    :return:
    '''
    d = {}
    userList = AccountList()
    for each in userList:
        u = loadUserFromFile(each)
        if isinstance(u,User):
            d.update({
                u.id:{
                    "name":u.name,
                    "tel":u.tel,
                    "email":u.email,
                }
            })
    createUserTable(d)

def judgeEmailOrlTel(index):
    if isinstance(index,int):
        if len(str(index))==11:
            return None,str(index)
    elif isinstance(index,str):
        if "@" in index:
            return index,None
        else:
            try:
                _ = int(index)
                return None,index
            except:
                return None,None
    return None,None

def createUser(name:str,password:str,index1=None,index2=None):
    email = None
    tel = None
    if isinstance(index1,str):
        if "@" in index1:
            email = index1
        elif len(index1)==11:
            try:
                _ = int(index1)
                tel = index1
            except:
                pass
    if isinstance(index2,str):
        if "@" in index2:
            email = index2
        elif len(index2)==11:
            try:
                _ = int(index2)
                tel = index2
            except:
                pass
    return createAccount(name,password,email=email,tel=tel)

def loadAccountByID(id):
    fileName = AccountDIR+id+".tbs"
    if os.path.exists(fileName):
        with open(fileName,"rb") as f:
            u = pickle.loads(f.read())
            return u
    return None

def changeEmailForUserTable(email,id,table=None):
    if table==None:
        table = loadUsertable()
    if id in table:
        table[id]["email"]=email
    createUserTable(table)

def changeTelForUserTable(Tel,id,table=None):
    if table==None:
        table = loadUsertable()
    if id in table:
        table[id]["tel"]=Tel
    createUserTable(table)

def changeIndexForUserTable(index,id):
    tel=None
    email = None
    if isinstance(index,int):
        if len(str(index))==11:
            tel = str(index)
    elif isinstance(index,str):
        if "@" in index:
            email=index
        else:
            try:
                _ = int(index)
                if len(str(index))==11:
                    tel=index
            except:
                pass
    if tel!=None:
        changeTelForUserTable(tel,id)
    if email !=None:
        changeEmailForUserTable(email,id)