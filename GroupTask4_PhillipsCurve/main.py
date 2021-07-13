from math import sqrt, exp, fabs
import numpy as np
import csv

import scipy
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import random

x = []
y = []

'''

with open('FPCPITOTLZGDEU.csv') as csvfile: #Германия
    reader = csv.DictReader(csvfile)
    for row in reader:
        y.append(float(row['FPCPITOTLZGDEU']))
with open('LMUNRRTTDEQ156S.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(float(row['LMUNRRTTDEQ156S']))
'''
'''
with open('FPCPITOTLZGUSA.csv') as csvfile: #США
    reader = csv.DictReader(csvfile)
    for row in reader:
        y.append(float(row['FPCPITOTLZGUSA']))
with open('NROU.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(float(row['NROU']))

'''

with open('FPCPITOTLZGJPN.csv') as csvfile: #Япония
    reader = csv.DictReader(csvfile)
    for row in reader:
        y.append(float(row['FPCPITOTLZGJPN']))
with open('LRUN64TTJPM156S.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(float(row['LRUN64TTJPM156S']))
        '''

with open('FPCPITOTLZGRUS.csv') as csvfile: #Россия
    reader = csv.DictReader(csvfile)
    for row in reader:
        y.append(float(row['FPCPITOTLZGRUS']))
with open('LRUN74TTRUM156N.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(float(row['LRUN74TTRUM156N']))

'''

X = np.array(x).reshape(-1,1)


Y = np.array(y)
model1 = LinearRegression().fit(X, Y)
poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(X)
model2 = LinearRegression()
model2.fit(x_poly,Y)

i = 0
y_0 = y
x_0 = x
for y0 in y:
    if y0 == 0:
        x_0.pop(i)
        y_0.pop(i)
        i-=1
    i+=1
expo = np.polyfit(x_0, np.log(y_0), 1, w=np.sqrt(y_0))

y_pred3 = []

for x1 in x:
    y_pred3.append(exp(expo[1]) * exp(expo[0] * x1))

y_pred1 = model1.predict(X).tolist()
y_pred2 = model2.predict(x_poly).tolist()

dists1 = []
dists2 = []
dists3 = []
for j in range(len(x)):
    dists1.append(fabs(y_pred1[j] - y[j]))
    dists2.append(fabs(y_pred2[j] - y[j]))
    dists3.append(fabs(y_pred3[j] - y[j]))
dists = [round(np.std(dists1), 5), round(np.std(dists2), 5), round(np.std(dists3), 5)]
min_dist = float('inf')
i = 0
indexs = []
for dist in dists:
    if dist < min_dist:
        min_dist = dist
for dist in dists:
    if dist > min_dist - 0.01 and dist < min_dist + 0.01:
        indexs.append(i)
    i+=1

if indexs.count(0) != 0:
    print('Линейное приближение достаточно хорошо')
if indexs.count(1) != 0:
    print('Полиномиальное приближение достаточно хорошо')
if indexs.count(2) != 0:
    print('Экспоненциальное приближение достаточно хорошо')

size = 3
trans = 1
scatter1 = plt.plot(x, y_pred1, c = 'red', label = u'Линейная регрессия')

scatter1 = plt.scatter(x, y, c='blue', s = size, alpha = trans, label = u'Исходные точки')
x.sort()
X = np.array(x).reshape(-1,1)
scatter1 = plt.plot(x, model2.predict(poly_reg.fit_transform(X)), c = 'green', label = u'Полиномиальная регрессия')
y_pred3 = []
for x1 in x:
    y_pred3.append(exp(expo[1]) * exp(expo[0] * x1))
scatter1 = plt.plot(x, y_pred3, c = 'yellow', label = u'Экспоненциальная регрессия')
plt.grid(True)
plt.xlabel(u'Уровень безработицы, %')
plt.ylabel(u'Темп инфляции, %')
plt.title(u'Взаимосвязь между инфляцией и безработицей в Японии в 1970-2019 годах', fontsize = 10)
plt.legend()
plt.show()
