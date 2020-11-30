import json,random
import matplotlib.pyplot as plt
from SportsData.heartDataType import Heart_Rate


# 读取standardHeartRateData
def getRandomData(returnDICT = False):
    path = "./DataBase/standard.json"

    with open(path, "r") as f:
        data = json.loads(f.read())["data"]

    meanValue = sum(data[50:]) / len(data[50:])
    high = max(data[50:])
    low = min(data[50:])

    randomData = []
    for i in range(len(data)):
        if i == 1:
            randomData.append(int(data[i] + random.randint(0, 10)))
        elif i == 2:
            randomData.append(int(data[i] + random.randint(5, 15)))
        elif i == 3:
            randomData.append(int(data[i] + random.randint(10, 20)))
        if i >= 50:
            randomData.append(int(data[i] + random.randint(-20, 20)))
        randomData.append(int(data[i]))
    HD = []
    for i in range(len(randomData)):
        heartdata = Heart_Rate(value=randomData[i], id=i)
        if randomData[i] < 125:
            heartdata.aerobic = 1
        elif randomData[i] > 150:
            heartdata.aerobic = -1
        else:
            heartdata.aerobic = 1 - (randomData[i] - 125) / 25
        if returnDICT:
            HD.append(heartdata.Dict)
        else:
            HD.append(heartdata)
    return HD