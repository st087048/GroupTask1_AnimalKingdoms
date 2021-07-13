import numpy as np
import random

def amountTestDeterminer(amountPoints):
    if amountPoints <= 1000: return amountPoints // 10
    elif amountPoints <= 10000: return amountPoints // 100
    elif amountPoints <= 1000000: return amountPoints // 1000
    else: return amountPoints // 100000


def usual(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)

    Points = np.random.randint(5, 1000, (amountPoints, 3))
    testPoints = np.random.randint(5, 1000, (amountTestPoints, 3))
    for point in Points: point[2] = 100
    for point in testPoints: point[2] = 100

    return Points, testPoints


def line(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)
    Points = np.zeros((amountPoints, 3))
    testPoints = np.zeros((amountTestPoints, 3))

    for i in range(amountPoints):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000)
        Points[i][2] = 100
    for i in range(amountTestPoints):
        testPoints[i][0] = random.randint(0, amountPoints)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000)
        testPoints[i][2] = 100

    return Points, testPoints

def lines3(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)
    Points = np.zeros((amountPoints, 3))
    testPoints = np.zeros((amountTestPoints, 3))

    for i in range(amountPoints//3):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000)
        Points[i][2] = 100
    for i in range(amountPoints//3, amountPoints//3*2):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000) + 50000
        Points[i][2] = 100
    for i in range(amountPoints//3*2, amountPoints):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000) + 100000
        Points[i][2] = 100

    for i in range(amountTestPoints//3):
        testPoints[i][0] = random.randint(0, amountPoints//3)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000)
        testPoints[i][2] = 100
    for i in range(amountTestPoints//3, amountTestPoints//3*2):
        testPoints[i][0] = random.randint(amountPoints//3, amountPoints//3*2)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000) + 50000
        testPoints[i][2] = 100
    for i in range(amountTestPoints//3*2, amountTestPoints):
        testPoints[i][0] = random.randint(amountPoints//3*2, amountPoints)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000) + 100000
        testPoints[i][2] = 100

    return Points, testPoints


def circles(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)

    Points = np.zeros((amountPoints, 3))
    testPoints = np.zeros((amountTestPoints, 3))

    for i in range(amountPoints//4):
        Points[i][0] = random.randint(0,2000)
        Points[i][1] = np.math.sqrt(1000000 - (Points[i][0] - 1000) * (Points[i][0] - 1000)) + random.randint(-50, 50)
        Points[i][2] = 100
    for i in range(amountPoints//4, amountPoints//2):
        Points[i][0] = random.randint(0,2000)
        Points[i][1] = - np.math.sqrt(1000000 - (Points[i][0] - 1000) * (Points[i][0] - 1000)) + random.randint(-50, 50)
        Points[i][2] = 100
    for i in range(amountPoints//2, amountPoints//4*3):
        Points[i][0] = random.randint(700, 1300)
        Points[i][1] = np.math.sqrt(100000 - (Points[i][0] - 1000) * (Points[i][0] - 1000)) + random.randint(-20, 20)
        Points[i][2] = 100
    for i in range(amountPoints//4*3, amountPoints):
        Points[i][0] = random.randint(700, 1300)
        Points[i][1] = - np.math.sqrt(100000 - (Points[i][0] - 1000) * (Points[i][0] - 1000)) + random.randint(-20, 20)
        Points[i][2] = 100


    for i in range(amountTestPoints//4):
        testPoints[i][0] = random.randint(0,2000)
        testPoints[i][1] = np.math.sqrt(1000000 - (testPoints[i][0] - 1000) * (testPoints[i][0] - 1000)) + random.randint(-50, 50)
        testPoints[i][2] = 100
    for i in range(amountTestPoints//4, amountTestPoints//2):
        testPoints[i][0] = random.randint(0, 2000)
        testPoints[i][1] = - np.math.sqrt(1000000 - (testPoints[i][0] - 1000) * (testPoints[i][0] - 1000)) + random.randint(-50, 50)
        testPoints[i][2] = 100
    for i in range(amountTestPoints//2, amountTestPoints//4*3):
        testPoints[i][0] = random.randint(700, 1300)
        testPoints[i][1] = np.math.sqrt(100000 - (testPoints[i][0] - 1000) * (testPoints[i][0] - 1000)) + random.randint(-20,20)
        testPoints[i][2] = 100
    for i in range(amountTestPoints//4*3, amountTestPoints):
        testPoints[i][0] = random.randint(700, 1300)
        testPoints[i][1] = - np.math.sqrt(100000 - (testPoints[i][0] - 1000) * (testPoints[i][0] - 1000)) + random.randint(-20,20)
        testPoints[i][2] = 100

    return Points, testPoints
