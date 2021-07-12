import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import pointGenerator

def closestPointX10(Point):
    distances = np.zeros((amountPoints, 2))
    testDistances = np.zeros((amountTestPoints, 2))
    for j in range(amountPoints):
        distances[j][0] = np.hypot(abs(Point[0]-Points[j][0]), abs(Point[1]-Points[j][1]))
        distances[j][1] = j
    for j in range(amountTestPoints):
        testDistances[j][0] = np.hypot(abs(Point[0]-testPoints[j][0]), abs(Point[1]-testPoints[j][1]))
        testDistances[j][1] = j
    distances = np.append(distances, testDistances, axis=0)
    distances = sorted(distances, key=lambda element: element[0])
    testDistances = sorted(testDistances, key=lambda element: element[0])
    return testDistances[0], distances[1:11]


amountPoints = 1000
amountTestPoints = amountPoints//10
amountClusters = int(input())
Points, testPoints = pointGenerator.circles(amountPoints)


cluster = AgglomerativeClustering(n_clusters=amountClusters, affinity='euclidean', linkage='ward')
testPointsClusters = np.array(cluster.fit_predict(testPoints))
plt.figure(figsize=(8, 8))
plt.scatter(testPoints[:,0], testPoints[:,1],  c=cluster.labels_, cmap='rainbow', marker='x')

for i in range(5):
    for point in Points:
        kInClusters = np.zeros((amountClusters))
        testneighbour, neighbours = closestPointX10(point)

        for neighbour in neighbours:
            if Points[int(neighbour[1])][2] < amountClusters:
                kInClusters[int(Points[int(neighbour[1])][2])] += 1

        kInClusters[testPointsClusters[int(testneighbour[1])]] += 3

        point[2] = kInClusters.argmax()


plt.scatter(Points[:,0], Points[:,1], c=Points[:,2], cmap='rainbow', s=2)


#_________The model of perfect clustering_________
plt.figure(figsize=(8, 8))
clusterModel = AgglomerativeClustering(n_clusters=amountClusters, affinity='euclidean', linkage='ward')
ModelClusters = np.array(clusterModel.fit_predict(Points))
plt.scatter(Points[:,0], Points[:,1], c=clusterModel.labels_, cmap='rainbow', s=2)
#_________________________________________________


plt.show()