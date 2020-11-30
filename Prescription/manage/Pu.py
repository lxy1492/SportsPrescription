import os,json
from Moudle.sportMoudle import Sport
from Prescription.manage import getSport
from SportsPrescription.config import prescription

PuPath = prescription["Pu"]

def Pu_compute():
    '''
    计算每个运动效果属性的百分比
    :return:
    '''
    sports = getSport.loadAllSports()
    num = len(sports)
    # print(num)
    u = {}
    for eachSport in sports:
        if isinstance(eachSport,Sport):
            if isinstance(eachSport.effect,list):
                for eachEffect in eachSport.effect:
                    if eachEffect not in u:
                        u.update({eachEffect:1})
                    else:
                        u[eachEffect]+=1
    # print(u)
    for each in u:
        u[each]=u[each]/num
    with open(PuPath,"w") as f:
        f.write(json.dumps(u))
    return u

def loadPu():
    if os.path.exists(PuPath):
        with open(PuPath,"r") as f:
            try:
                return json.loads(f.read())
            except:
                return -1
    return -2

def getPu():
    return loadPu()

if __name__ == '__main__':
    os.chdir("../../")
    print(Pu_compute())
