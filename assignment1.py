# Roll no.- 16EE30010
# Name - Harsh Maheshwari
# Assignment Number - 1
# Enter the complete file name in double quotes
# The output is given assuming the starting index is 1
import csv 

a = []
row_prev = []
j = 0
# data = input('Enter input file name : ')
with open("data1.csv", 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		#print(row[8])
		if j == 0: 
			row_prev = row
			a = row
			#print row[8]
		if row[8] == '1':
			#print("Entered")
			for i in range(8):
				if a[i] != row[i]:
					a[i] = '2'
		row_prev = row
		j = j+1
	#print a
	b = []
	for i in range(8):
		if a[i] == '1':
			b.append(i+1)
		if a[i] == '0':
			b.append(-1*(i+1))
	d = len(b)
	c = []
	c.append(d)
	for i in range (d):
		c.append(b[i])
	print c
				
			
