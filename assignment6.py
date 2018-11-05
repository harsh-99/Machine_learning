import numpy as np 
import time

num_epochs = 10
data = np.genfromtxt('data6.csv', delimiter = ',')
X = data[:, 0 : data.shape[1] - 1]
Y = data[:, data.shape[1] - 1].reshape([-1,1])
num_features = X.shape[1]

print("Data shape:" + str(data.shape))
print("X shape:" + str(X.shape))
print("Y shape:" + str(Y.shape))
j=0
w = np.random.rand(X.shape[1],1)
tic = time.time()
for j in range(num_epochs):
	a = np.dot(X,w)
	acc = 0
	y = 1/(1+np.exp(-a))
	loss = 0.5*np.power((Y-y),2)
	for i in range(X.shape[0]):
		gradient = -((Y[i].reshape([-1,1]))-(y[i].reshape([-1,1])))*(y[i].reshape([-1,1]))*(1-(y[i].reshape([-1,1])))*(X[i].reshape([-1,1]))
		w = w-(0.2*gradient)
		# print w	
	y = np.around(y)
	for i in range(X.shape[0]):
		if y[i] == Y[i]:
			acc+=1
	print float(acc)/float(X.shape[0])	

print("Time is "+str(time.time()-tic))
print("**************")
X_test = np.genfromtxt('test6.csv', delimiter = ',')
print(X_test.shape)
a_test = np.dot(X_test,w)
print(a_test.shape)
y_test = 1/(1+np.exp(-a_test))
final = np.around(y_test)
f= open("16EE30010_6.out", "w+")
for i in range(final.shape[0]):
	f.write(str(int(final[i]))+ "  ")
f.close()
# print loss
# print(loss.shape)