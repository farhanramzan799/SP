#!usr/bin/python
import numpy as np
mat=[[10,20,30,40,50,60,70,80],
	[11,21,31,41,51,61,71,81],
	[12,22,32,42,52,62,72,82],
	[13,23,33,43,53,63,73,83],
	[14,24,34,44,54,64,74,84],
	[15,25,35,45,55,65,75,85],
	[16,26,36,46,56,66,76,86],
	[17,27,37,47,57,67,77,87]]

print mat[2][3]
n=2
a=[[0]* n for i in range(n)]
for i in range(n):
	for j in range(n):
		a[i][j]=int(input())
		
print (np.matrix(a))

for i,j in enumerate(mat):
	for k,l in enumerate(j):
		if a[0][0]==l:
			if a[0][1]==mat[i][k+1] and a[1][0]==mat[i+1][k] and a[1][1]==mat[i+1][k+1]:
				print "2*2 exists in 8*8 matrix."
			else:
				print "2*2 matrix doesnot exists in 8*8 matrix."

