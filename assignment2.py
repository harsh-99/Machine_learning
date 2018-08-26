# 16EE30010
# Harsh Maheshwari
# Assignment Number 2
# Compilation : python <program_name>

import numpy as np
import math

class Parent:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def PrintTree(self):
		if(self.left):
			self.left.PrintTree()
		print self.data
		if(self.right):
			self.right.PrintTree()

def entropy(w, r):
		if(w == 0 and r == 0):
			return 0
		elif(w == 0):
			return 0#-(w/(w+r))*math.log((w/(w + r)), 2)
		elif(r == 0):
			return 0#-(w/(w+r))*math.log((w/(w + r)), 2)
		else:
			return -(w/(w+r))*math.log((w/(w + r)), 2) -(w/(w+r))*math.log((w/(w + r)), 2)


data = np.genfromtxt('data2.csv', delimiter = ',')
X = data[:, 0 : data.shape[1] - 1]
Y = data[:, data.shape[1] - 1]
num_features = X.shape[1]
mark = np.zeros([1, num_features], dtype = np.int32)
# print data
# print X

def function(X, Y, visited):
	if(X.shape[1] == len(visited)):
		# print "All_visited"
		return None
	a1 = a2 = 1
	for i in range(0, Y.shape[0]):
		if(Y[i] == 1):
			a1 = 0
		else:
			a2 = 0

	if(a1):
		# print "Pure negative"
		return Parent(-1)
	if(a2):
		# print "Pure Positive"
		return Parent(-2)
	E_class = 0.0
	p = n = 0.0
	for i in range(0, X.shape[0]):
		if(Y[i] == 1):
			p += 1
		else:
			n += 1
	E_class = entropy(p, n)
	# print("Target Entropy : ", E_class)
	max_gain = -1
	max_gain_attr = -1
	for i in range(0, X.shape[1]):
		if(i in visited):
			continue
		p1 = n1 = p2 = n2 = pos = neg = 0.0
		for j in range(0, X.shape[0]):
			if(X[j][i] == 0):
				neg += 1
				if(Y[j] == 1):
					p1 += 1
				else:
					n1 += 1
			else:
				pos += 1
				if(Y[j] == 1):
					p2 += 1
				else:
					n2 += 1

		neg_entropy = entropy(p1, n1)
		pos_entropy = entropy(p2, n2)
		weighted = (pos/(pos + neg))*pos_entropy + (neg/(pos + neg))*neg_entropy
		gain = E_class - weighted
		if(max_gain < gain):
			max_gain = gain
			max_gain_attr = i
		# print gain
	# print "Max gain = ", max_gain
	# print "Max gain_attr = ", max_gain_attr
	visited.append(max_gain_attr)
	root = Parent(max_gain_attr)
	X_pos = []
	X_neg = []
	Y_pos = []
	Y_neg = []
	for i in range(0, X.shape[0]):
		if(X[i][max_gain_attr] == 0):
			X_neg.append(X[i])
			Y_neg.append(Y[i])
		else:
			X_pos.append(X[i])
			Y_pos.append(Y[i])
	X_neg = np.reshape(np.array(X_neg), (-1, X.shape[1]))
	X_pos = np.reshape(np.array(X_pos), (-1, X.shape[1]))
	Y_neg = np.array(Y_neg)
	Y_pos = np.array(Y_pos)
	root.left = function(X_neg, Y_neg, visited)
	root.right = function(X_pos, Y_pos, visited)

	return root

# print Y.shape
# print X.shape
root = function(X, Y, [])
test = np.genfromtxt('test2.csv', delimiter = ',')
ans = []
for i in range(0, test.shape[0]):
	temp = root
	while(temp):
		if(temp.data == -1):
			ans.append(0)
			break
		if(temp.data == -2):
			ans.append(1)
			break
		temp = temp.left if test[i][temp.data] == 0 else temp.right
print(ans)
