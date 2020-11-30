import os,pickle
from Moudle.sportMoudle import Sport

class Course():
    def __init__(self,name,description=None,difficulty=None,saveDIR=None,pioneer=None):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.Sports = None
        self.saveDIR = saveDIR
        self.pioneer = pioneer

    @ property
    def Dict(self):
        d = {
            "name":self.name,
            "description":self.description,
            "Sports":self.Sports,
            "saveDIR":self.saveDIR,
            "pioneer":self.pioneer,
            "difficulty":self.difficulty,
        }
        return d

    def setName(self,v):
        if isinstance(v,str):
            self.name = v
            return 0
        return -1

    def setDescription(self,s):
        if isinstance(s,str):
            self.description = s
            return 0
        return -1

    def setDifficulty(self,v):
        if isinstance(v,float):
            if v>=0:
                self.difficulty = v
                return 0
            return -1
        elif isinstance(v,int):
            if v>=0:
                self.difficulty = float(v)
                return 0
            return -1
        elif isinstance(v,str):
            try:
                return self.setDifficulty(float(v))
            except:
                return -1
        return -1

    def __str__(self):
        string = "course:"+self.name
        return string

    def setSports(self,data):

        if isinstance(data,list):
            l = []
            for each in data:
                if isinstance(each,Sport):
                    l.append(each)
            if self.Sports!=None:
                for each in l:
                    if not each in self.Sports:
                        self.Sports.append(each)
            else:
                self.Sports = l
            return 0
        elif isinstance(data,Sport):
            if self.Sports==None:
                self.Sports = [data]
            else:
                if not data in self.Sports:
                    self.Sports.append(data)
            return 1

        elif isinstance(data,dict):
            for each in data:
                if isinstance(data[each],Sport):
                    if self.Sports!=None:
                        if not data[each] in self.Sports:
                            self.Sports.append(data[each])
                    else:
                        self.Sports = [data[each]]
            return 2
        return -1

    def setPioneer(self,v):
        if isinstance(v,str):
            self.pioneer = v
            return 0
        return -1

    def save(self):
        if not os.path.exists(self.saveDIR):
            os.makedirs(self.saveDIR)
        filePath = os.path.join(self.saveDIR,self.name+".tbs")
        with open(filePath,'wb') as f:
            f.write(pickle.dumps(self))
        return 0

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