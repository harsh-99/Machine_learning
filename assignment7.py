# 16EE30010
# Harsh Maheshwari
# Assignment Number 7
# Compilation : python <program_name>

import numpy as np
import math

k = 2
iteration = 10
a = []
grp1 = []
grp2 = []

data = np.genfromtxt('data7.csv', delimiter = ',')
X = data[:,:]
num_features = X.shape[1]

def euclideanDistance(data1, data2, length):
    distance = 0
    # print(data1[0])
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    # print(np.sqrt(distance))
    return np.sqrt(distance)

def calculateMean(group, X):
	mean = [0]
	for i in range(len(group)):
		mean = np.add(mean, X[group[i],:])
	mean = mean*1.0/X.shape[1]
	return mean

a = np.random.randint(0,X.shape[0],size=k)
centre1 = X[a[0],:]
centre2 = X[a[1],:]

for i in range(iteration):
	print("The iteration is " + str(i))
	grp1 = []
	grp2 = []
	for j in range(X.shape[0]):
		a1 = euclideanDistance(centre1, X[j,:], num_features)
		a2 = euclideanDistance(centre2, X[j,:], num_features)
		if a1>=a2:
			grp2.append(j)
		else :
			grp1.append(j)
	mean1 = calculateMean(grp1,X)
	mean2 = calculateMean(grp2,X)
	centre1 = mean1
	centre2 = mean2

print grp1
print grp2
output = np.zeros(X.shape[0])
for i in range(len(grp1)):
	output[grp1[i]] = 1
for i in range(len(grp2)):
	output[grp2[i]] = 2
print output.shape
output.reshape([-1,1])	
f= open("16EE30010_7.out", "w+")
for i in range(output.shape[0]):
	f.write(str(int(output[i]))+ "  ")
f.close()

