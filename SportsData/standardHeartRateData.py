# 直接生成标准的运动数据
import os,json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def createBaseLine():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    y = [80, 90, 130, 160, 144, 139, 134, 140, 133, 142, 129, 135, 140, 138, 132, 138, 142, 133, 132, 138, 142, 137,
         133, 138, 142, 134, 139]
    x = np.array(x).reshape([len(x), 1])
    y = np.array(y)

    degree = 6
    poly_reg = PolynomialFeatures(degree=degree)
    x_poly = poly_reg.fit_transform(x)
    lin_reg2 = LinearRegression()

    lin_reg2.fit(x_poly, y)
    return lin_reg2,len(x)


def createDeclineHeartData():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
    y = [138, 126, 112, 99, 93, 92, 89, 101, 123, 133, 138]
    x = np.array(x).reshape([len(x), 1])
    y = np.array(y)

    degree = 6
    poly_reg = PolynomialFeatures(degree=degree)
    x_poly = poly_reg.fit_transform(x)
    lin_reg2 = LinearRegression()

    lin_reg2.fit(x_poly, y)
    return lin_reg2,len(x)


def createData(uid="10001",prescription="10001",startTime="2020-06-30 18:12"):
    baseLine,xRange = createBaseLine()
    declineLine,xRange1 = createDeclineHeartData()
    data = []
    reg = PolynomialFeatures(degree=6)
    for i in range(xRange):
        y = baseLine.predict(reg.fit_transform(np.array([i]).reshape([1,1])))
        try:
            y = y.tolist()[0]
            data.append(y)
        except:
            pass
    start = 6
    x = start
    end = 26
    i = 0
    while(i<20000):
        y = baseLine.predict(reg.fit_transform(np.array([x]).reshape([1, 1])))
        try:
            y = y.tolist()[0]
            data.append(y)
        except:
            pass
        i += 1
        x += 1
        if x>end:
            x = start
    return {
        "uid":uid,
        "prescription":prescription,
        "startTime":startTime,
        "data":data,
    }





if __name__ == '__main__':
    os.chdir("../")
    data = createData()
    path = "./DataBase/standard.json"
    with open(path,"w") as f:
        f.write(json.dumps(data))