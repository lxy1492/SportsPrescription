from Moudle.sportMoudle import Sport,target,effect
from Prescription.manage import getSport

def initQuantization(num:int)->list:
    l = []
    for i in range(num):
        l.append(0)
    return l

def getQuantization(property:list,all:list):
    if isinstance(property,list) and isinstance(all,list):
        length = len(property)
        if length<=len(all):
            quantization = initQuantization(len(all))
            if isinstance(quantization,list):
                for i in range(len(quantization)):
                    if all[i] in property:
                        quantization[i]=1
                    else:
                        quantization[i]=0
                return quantization
    return None

# 计算作用对象向量
def computeT():
    sports = getSport.loadAllSports()
    for each in sports:
        if isinstance(each,Sport):
            r = getQuantization(each.target,target)
            if r!=None:
                each.T = r
                each.save()

# 计算效果属性向量
def computeE():
    sports = getSport.loadAllSports()
    for each in sports:
        if isinstance(each,Sport):
            r = getQuantization(each.effect,effect)
            if r!=None:
                each.E = r
                each.save()

if __name__ == '__main__':
    import os
    os.chdir("../../")
    computeE()
    computeT()