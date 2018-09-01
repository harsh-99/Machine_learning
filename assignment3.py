# 16EE30010 
# Harsh Maheshwari 
# Assignment no. 3
# Compilation : python <program_name>

import numpy as np
data = np.genfromtxt('data3.csv', delimiter = ',')
X = data[:,0:data.shape[1]-1]
Y = data[:, data.shape[1]-1]
num_yes = np.count_nonzero(Y)
# print("daskjn",num_yes)
num_no = Y.shape[0] - np.count_nonzero(Y)
prob_yes = float(np.count_nonzero(Y))/float(Y.shape[0])
prob_no = 1-prob_yes
save_pos = []    #to save probability when label of class is 1. In this even index for yes and odd for no 
save_neg = []	 #to save probability when label of class is 0. In this even index for yes and odd for no
for i in range (X.shape[1]):
	p1=n1=p2=n2=pos=neg=0
	for j in range (X.shape[0]):
		if (X[j][i]==0):
			neg = neg+1
			if (Y[j] == 1):
				p1=p1+1
			else:
				n1 = n1+1
		else :
			pos= pos+1
			if(Y[j] == 1):
				p2 = p2+1
			else :
				n2 = n2+1
	# print(p2)
	prob1 = float(p2+1)/float(num_yes+2)    #added 1 for add-1 smoothing
	prob2 = float(n2+1)/float(num_no+2)	
	save_pos.append(prob1)
	save_pos.append(prob2)
	prob3 = float(p1+1)/float(num_yes+2)
	prob4 = float(n1+1)/float(num_no+2)
	save_neg.append(prob3)
	save_neg.append(prob4)
	# print(save_pos)
	# print(p1+p2)	
	# print(n1+n2)		
# j=0
# print(save_pos)
# print(save_neg)
# print(save_pos[15])
i =0
j =0
test = np.genfromtxt('test3.csv', delimiter = ',')
for i in range(test.shape[0]):
	prob_final_yes = 1
	prob_final_no = 1
	for j in range (test.shape[1]):									
		if (test[i][j] == 0):
			prob_final_yes = prob_final_yes*save_neg[j*2]
			prob_final_no = prob_final_no*save_neg[(j*2)+1]
		else:
			prob_final_yes = prob_final_yes*save_pos[j*2]
			prob_final_no = prob_final_no*save_pos[(j*2)+1]
	# print(j)	
	prob_final_no = prob_final_no*prob_no
	prob_final_yes = prob_final_yes*prob_yes
	# print(prob_final_yes)
	# print(prob_final_no)
	if (prob_final_yes > prob_final_no):
		print("the output for column "+ str(i) + " is", 1)
	else:
		print("the output for column "+ str(i) + " is", 0)

