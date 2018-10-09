import numpy as np
from sklearn import preprocessing

data = np.genfromtxt('spambase/spambase.csv', delimiter = ',')
X = data[:, 0 : data.shape[1] - 1]
Y = data[:, data.shape[1] - 1].reshape([-1,1])
num_features = X.shape[1]
acc = 0

print("Data shape:" + str(data.shape))
print("X shape:" + str(X.shape))
print("Y shape:" + str(Y.shape))

X = preprocessing.normalize(X)
for i in range (X.shape[1]):
	print("The max for the column "+ str(i) + " is " + str(X[np.argmax(X[:,i]),i]))

perms = np.random.permutation(data.shape[0])
print("printing random permutation" )
print(perms)

X_random = X[perms,:]
Y_random = Y[perms,:]
trianing_id = int(data.shape[0]*0.7)
X_train = X_random[0:trianing_id,:]
Y_train  = Y_random[0:trianing_id,:]
X_val = X_random[(trianing_id+1):data.shape[0],:]
Y_val = Y_random[(trianing_id+1):data.shape[0],:]

print("X_train shape:"+str(X_train.shape))
print("Y_train shape:" + str(Y_train.shape))
print("X_val shape:" + str(X_val.shape))
print("Y_val shape" + str(Y_val.shape))

#Import Library
from sklearn import svm
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object 
model = svm.SVC(kernel='linear', C=1, gamma=1) 
model.fit(X_train, Y_train)
model.score(X_train, Y_train)
print("Completed")
# #Predict Output
predicted= model.predict(X_val)
predicted = predicted.reshape([-1,1])
print(predicted.shape)
for i in range (predicted.shape[0]):
	if predicted[i,0] == Y_val[i,0]:
		acc +=1
print("The accuracy obtained is "+str(float(acc)/float(predicted.shape[0])) )


