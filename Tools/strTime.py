import time

def getChineseLocalStrTime()->(str,str):
    t = time.localtime()
    year = t.tm_year
    mon = t.tm_mon
    day = t.tm_mday
    H = t.tm_hour
    M = t.tm_min
    S = t.tm_sec
    date = str(year)+"年"+str(mon)+"月"+str(day)+"日"
    time_ = str(H)+"时"+str(M)+"分"+str(S)+"秒"
    return date,time_