# 16EE30010
# Harsh Maheshwari
# Assignment Number 4
# Compilation : python <program_name>


import numpy as np
import math

k = 5
data = np.genfromtxt('data4.csv', delimiter = ',')
X = data[:, 0 : data.shape[1] - 1]
Y = data[:, data.shape[1] - 1]
num_features = X.shape[1]

data_test = np.genfromtxt('test4.csv', delimiter = ',')
X_test = data_test[:,:]
y_predicted = []
# print (X_test[5,:])

def euclideanDistance(data1, data2, length):
    distance = 0
    # print(data1[0])
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    # print(np.sqrt(distance))
    return np.sqrt(distance)
# print(X_test.shape[0])

for i in range(X_test.shape[0]):
	difference = []
	least_five = np.zeros((5,2))
	count_0 = 0
	count_1 = 0
	for j in range(X.shape[0]):
		dist = euclideanDistance(X_test[i,:], X[j,:], num_features)
		difference.append(dist)
	# print(difference)
	# print(difference[5])
	# print(len(difference))  			
	for x in range(k):
		minimum = 99999
		for a in range(len(difference)):
			if difference[a]<minimum:
				minimum = difference[a]
				index = a
		del difference[index]
		least_five[x, 0]= minimum
		least_five[x, 1]= Y[index]
		# print(len(difference))
		if Y[index] == 0:
			count_0 +=1
		else:
			count_1 +=1
		# print(minimum)

	if count_0 > count_1:
		y_predicted.append(0)
	else:
		y_predicted.append(1)

	# print(least_five)
print(y_predicted)	

for i in range(X_test.shape[0]):
	print("Test instance "+ str(i)+ ": " + str(y_predicted[i]))
