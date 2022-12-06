import numpy as np

def loadDataSet(filename):
    priceMat = []; caratMat = [];
    with open(filename) as f:
        for line in f:
            if line.startswith("Price"):
                continue
            instance = str.strip(line).split('\t')
            priceMat.append(float(instance[0]))
            caratMat.append([1.0, float(instance[1])])
    return caratMat, priceMat

def standRegres(xArr, yArr):
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:
        print('This matrix is singular, cannot do inverse')
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

xArr, yArr = loadDataSet('diamonds.txt')
ws = standRegres(xArr, yArr)

xMat = np.mat(xArr)
yHat = xMat * ws

print(ws)
print("x value = ", xArr[10][1], ", calc value = ", yHat[10], ", real value = ", yArr[10])
print("x value = ", xArr[1000][1], ", calc value = ", yHat[1000], ", real value = ", yArr[1000])
print("x value = ", xArr[2300][1], ", calc value = ", yHat[2300], ", real value = ", yArr[2300])
