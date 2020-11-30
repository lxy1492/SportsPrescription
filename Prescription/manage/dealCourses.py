import os
from SportsPrescription.config import prescription as config
from Prescription.manage import getCourse,getSport
from Moudle.courseMoudle import Course
from Moudle.sportMoudle import Sport

def loadAllCourses():
    coursesList = getCourse.getCourseList()
    l = []
    for each in coursesList:
        # print(each)
        c = getCourse.loadCourse(each,returnDict=False)
        if isinstance(c,Course):
            l.append(c)
    return l

def setBelong(s,c):
    if isinstance(s,str):
        s = getSport.loadSport(s,returnDict=False)
        if isinstance(s,Sport):
            pass
        else:
            return -1
    if isinstance(s,Sport):
        if isinstance(c,Course):
            s.setBelong(c.name)
            return 0
        elif isinstance(c,str):
            s.setBelong(c)
            return 0
        elif isinstance(c,list):
            for each in c:
                if isinstance(each,str):
                    s.setBelong(each)
                elif isinstance(each,Course):
                    s.setBelong(each.name)
            return 0
        else:
            return -1
        # if isinstance()
    else:
        return -2

def setAllSportsBelong():
    courses = loadAllCourses()
    for each in courses:
        if isinstance(each,Course):
            if each.Sports!=None:
                for eachSport in each.Sports:
                    if isinstance(eachSport,Sport):
                        s = eachSport
                    elif isinstance(eachSport,dict):
                        s = getSport.loadSport(eachSport["name"])
                    elif isinstance(eachSport,str):
                        s = getSport.loadSport(eachSport)
                    else:
                        continue
                    # s = getSport.loadSport(eachSport["name"])
                    setBelong(s,each)
                    s.save()
                    print("set",each.name,"-",eachSport.name)

if __name__ == '__main__':
    os.chdir("../../")
    setAllSportsBelong()