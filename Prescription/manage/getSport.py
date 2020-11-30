import os,re
import pickle
import base64
from Moudle.sportMoudle import Sport,target,effect
from SportsPrescription.config import prescription as config

#
# target = ["全身","背部","头部","颈部","肩部","胸部","腰部","臀部","手部","手腕","手掌","腿部","大腿","小腿","脚踝","脚掌"]
# effect = ["减脂瘦身","增肌","塑形","增强力量","调理身心","增强有氧能力","增强体质","增强耐力","强化心肺"]


def get_sport_list():
    pathDIR = config["sportDIR"]
    l = []
    for each in os.listdir(pathDIR):
        if each.split(".")[-1] == "tbs":
            l.append([each,pathDIR+each])
    return l

def loadSport(name:str,returnDict=True):
    if not ".tbs" in name:
        name = name+".tbs"
    path = config["sportDIR"]+name
    if not os.path.exists(path):
        # print(path)
        return None
    with open(path,"rb") as f:
        data = pickle.loads(f.read())
    if isinstance(data,Sport):
        if not returnDict:
            return data
        data = data.Dict
        data.pop("saveDIR")
        imageSRC = data["image"]
        img = None
        if isinstance(imageSRC,str):
            if os.path.exists(imageSRC):
                with open(imageSRC,"rb") as f:
                    img = f.read()
        if img!=None:
            img = base64.b64encode(img).decode()
            img = 'data:image/jpeg;base64,'+img
        data["image"] = img
        return data
    else:
        return None

def setEffect(name,type,effect):
    # print(name)
    if isinstance(name,str):
        s = loadSport(name,returnDict=False)
        # print(name)
        if isinstance(s,Sport):
            if type==True:
                s.setEffect(effect)
            else:
                if effect in s.effect:
                    s.effect.remove(effect)
            s.save()
            return s.Dict
    return None

def setTarget(name,type,target):
    if isinstance(name,str):
        s = loadSport(name,returnDict=False)
        # print(type)
        if isinstance(s,Sport):
            if type==True:
                # print(type)
                s.setTarget(target)
            else:
                # print("remove")
                if target in s.target:
                    if target=="全身":
                        s.target = []
                    elif target=="腿部":
                        if "小腿" in s.target:
                            s.target.remove("小腿")
                        if "大腿" in s.target:
                            s.target.remove("大腿")
                        s.target.remove(target)
                    else:
                        s.target.remove(target)
                    if "全身" in s.target:
                        if len(s.target)<len(target):
                            s.target.remove("全身")
            s.save()
            return s.Dict
    return None

def loadAllSports():
    l = get_sport_list()
    # print(l)
    sl = []
    for each in l:
        if isinstance(each[0],str):
            s = loadSport(each[0],returnDict=False)
            # print(s)
            if isinstance(s,Sport):
                # print(s)
                sl.append(s)
    return sl

if __name__ == '__main__':
    os.chdir("../../")
    # print(os.getcwd())
    print(loadSport("坐姿冲刺训练"))