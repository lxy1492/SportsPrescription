import os,pickle
from Moudle.courseMoudle import Course
from SportsPrescription.config import prescription as config

def getCourseList():
    path = config["courseDIR"]
    l = []
    for each in os.listdir(path):
        if ".tbs" in each:
            l.append(each.split(".tbs")[0])
    if len(l)>0:
        return l
    else:
        return None

def loadCourse(name,returnDict=True):
    if not isinstance(name,str) or isinstance(name,list):
        return None
    if isinstance(name,str):
        if not ".tbs" in name:
            name = name+".tbs"
        path = config["courseDIR"]+name
        try:
            with open(path,"rb") as f:
                c = pickle.loads(f.read())
            if returnDict==True:
                # print(c.Dict)
                data =  c.Dict
                data["Sports"] = []
                for each in c.Sports:
                    data["Sports"].append(each.Dict)
                data.pop("saveDIR")
                return data
            else:
                return c
        except:
            return None
    else:
        l = []
        for each in name:
            r = loadCourse(each,returnDict)
            if r!=None:
                l.append(r)
        return l



if __name__ == '__main__':
    os.chdir("../../")
    print(getCourseList())
    print(os.listdir(config["courseDIR"]))
