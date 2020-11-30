import os,pickle

target = ["全身","背部","头部","颈部","肩部","胸部","腰部","臀部","手臂","手腕","手掌","腿部","大腿","小腿","脚踝","脚掌"]
effect = ["减脂瘦身","平衡","减压","缓解疼痛","增肌","塑形","增强力量","调理身心","增强有氧能力","增强体质","增强耐力","强化心肺"]
sportType = ['有氧',"力量","柔韧"]

class Sport():
    def __init__(self,name,sportType=None,level=None,sportsTime=None,image=None,belong=None,saveDIR=None,strength=None,frequency=None):
        self.name = name
        self.sportsTime=sportsTime
        self.image = image
        self.belong = belong
        self.saveDIR=saveDIR
        self.difficulty = None
        self.detail = None
        self.effect= []
        self.target = []
        self.equipment = []
        self.site = None
        self.strength = strength
        self.frequency = frequency
        self.level = level
        # 运动效果onehot量化向量
        self.E = None
        # 作用对象onehot量化向量
        self.T = None
        # 运动处方类型
        self.sportType = sportType

    def setSportType(self,type_:str):
        if isinstance(type_,str):
            if type_ in sportType:
                self.sportType = type_
                return 0
            else:
                if "氧" in type_ and '无' in type_:
                    self.sportType="力量"
                    return 1
                elif "氧" in type_ and "无" not in type_:
                    self.sportType = "有氧"
                    return 1
                elif "柔" in type_ or "缓" in type_ or "韧" in type_:
                    self.sportType = "柔韧"
                    return 1
            return -1
        return -2

    def setStrength(self,v):
        if isinstance(v,int):
            v = float(v)
        elif isinstance(v,str):
            try:
                v = float(v)
            except:
                return -1
        if isinstance(v,float):
            if v<0:
                return -2
            else:
                self.strength = v
                return 0
        else:
            return -3

    def setFrequency(self,f):
        if isinstance(f,int):
            f = float(f)
        elif isinstance(f,str):
            f = float(f)
        if isinstance(f,float):
            if f>0:
                self.frequency = f
                return 0
            else:
                return -1
        return -2

    @ property
    def Dict(self):
        d = {
            "name":self.name,
            "sportsTime":self.sportsTime,
            "strength":self.strength,
            "frequency":self.frequency,
            "image":self.image,
            "belong":self.belong,
            "saveDIR":self.saveDIR,
            "difficulty":self.difficulty,
            "detail":self.detail,
            "effect":self.effect,
            "target":self.target,
            'equipment':self.equipment,
            "site":self.site,
        }
        return d
    def setDetil(self,d):
        self.detail = d

    def setName(self,n:str):
        if isinstance(n,str):
            self.name = n
            return 0
        return -1

    def setSaveDIR(self,dir):
        if isinstance(dir,str):
            if os.path.exists(dir):
                self.saveDIR = dir
                return 0
            else:
                try:
                    os.makedirs(dir)
                    return 1
                except:
                    return -1
        return -2

    def setSportsTime(self,t):
        self.sportsTime = t

    def setImage(self,path:str):
        if isinstance(path,str):
            self.image = path
            return 0
        return -1

    def setBelong(self,course:str):
        if isinstance(course,str):
            if self.belong!=None:
                self.belong.append(course)
            else:
                self.belong = [course]
        elif isinstance(course,list):
            for each in course:
                if isinstance(each,str):
                    if self.belong!=None:
                        self.belong.append(each)
                    else:
                        self.belong = [each]
        return 0

    def save(self):
        if not os.path.exists(self.saveDIR):
            os.makedirs(self.saveDIR)
        path = os.path.join(self.saveDIR,self.name+".tbs")
        with open(path,"wb") as f:
            f.write(pickle.dumps(self))
        return 0

    def __str__(self):
        string = 'sport:'+self.name+";"
        return string

    def setEffect(self,v):
        if isinstance(v,str):
            if v in effect:
                if self.effect==None:
                    self.effect = [v]
                    return 0
                elif isinstance(self.effect,list):
                    if not v in self.effect:
                        self.effect.append(v)
                        return 1
                    return 2
                return -1
            else:
                return -2
        elif isinstance(v,list):
            for each in v:
                self.setEffect(each)
        else:
            return -3

    def setTarget(self,t):
        if isinstance(t,str):

            if t in target:
                if self.target==None:
                    # 判断是否有自动填入
                    if t == "全身":
                        self.target = target
                        return 0
                    elif t == "腿部":
                        if not "腿部" in self.target:
                            self.target.append("腿部")
                        self.setTarget(["大腿", "小腿"])
                    else:
                        self.target = [t]
                    # 判断
                    if "大腿" in self.target and "小腿" in self.target:
                        if not "腿部" in self.target:
                            self.target.append("腿部")
                    if len(self.target) == len(target)-1:
                        if not "全身" in self.target:
                            self.target = target
                    return 0
                elif isinstance(self.target,list):
                    if not  t in self.target:
                        # 判断是否有自动填入
                        if t == "全身":
                            self.target = target
                            return 0
                        elif t == "腿部":
                            if not "腿部" in self.target:
                                self.target.append("腿部")
                            self.setTarget(["大腿", "小腿"])
                        else:
                            self.target.append(t)
                        # 检查
                        if "大腿" in self.target and "小腿" in self.target:
                            if not "腿部" in self.target:
                                self.target.append("腿部")
                        if len(self.target) == len(target) - 1:
                            if not "全身" in self.target:
                                self.target = target
                        return 1
                    return 2
                return -1
            else:
                return -2
        elif isinstance(t,list):
            for each in t:
                self.setTarget(each)
            return 3
        return -4