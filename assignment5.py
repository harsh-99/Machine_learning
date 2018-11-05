import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 

kernel = 'linear'

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
accuracy = []
accuracy_train = []
best_acc = 0
num = []
best_c = 0
best_train_acc = 0
best_c_train = 0

for j in range(200):
	model = svm.SVC(kernel=kernel, C=(j+1), gamma=7) 
	model.fit(X_train, Y_train)
	model.score(X_train, Y_train)
	predicted_train = model.predict(X_train)
	predicted_train = predicted_train.reshape([-1,1])
	predicted= model.predict(X_val)
	predicted = predicted.reshape([-1,1])
	print("Current Value of C is:" + str(j+1))
	print("Completed")
	# #Predict Output
	print(predicted.shape)
	acc = 0
	acc_train = 0
	for i in range (predicted_train.shape[0]):
		if predicted_train[i,0] == Y_train[i,0]:
			acc_train +=1
	for i in range (predicted.shape[0]):
		if predicted[i,0] == Y_val[i,0]:
			acc +=1
	
	print("The accuracy obtained is "+ str(float(acc)/float(predicted.shape[0])))
	print("the train accuracy is "+ str(float(acc_train)/float(predicted_train.shape[0])))
	accuracy.append(float(acc)/float(predicted.shape[0]))
	accuracy_train.append(float(acc_train)/float(predicted_train.shape[0]))
	
	if best_train_acc< float(acc_train)/float(predicted_train.shape[0]):
		best_train_acc = float(acc_train)/float(predicted_train.shape[0])
		best_c_train = j+1

	if best_acc<(float(acc)/float(predicted.shape[0])):
		best_acc = (float(acc)/float(predicted.shape[0]))
		best_c = j+1
	j +=1
	num.append(j)

print("Best accuracy achieved is:"+str(best_acc))
print("Best C is:"+str(best_c))
np.save('acc_' +str(kernel) +'.npy',accuracy)
plt.plot(num,accuracy, label = 'test')
plt.plot(num,accuracy_train, label = 'train')
plt.xlabel("C")
plt.ylabel("Accuracy")
plt.legend(loc="lower center")
plt.title(kernel)
plt.savefig('plot_'+str(kernel)+'_'+ str(best_c)+'_'+ str(best_acc)+'_'+ str(best_c_train)+'_'+ str(best_train_acc)+'.png', bbox_inches='tight')
plt.show()

