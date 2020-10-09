
def genmatrix(x,y):
	matrix=[]
	for i in range(x):
		matrix.append([])

		for j in range(y):
			matrix[i].append(i*j)
			
	print(matrix)


x=int(input("Please enter the 1st number : "))
y=int(input("Please enter the 2nd number : "))
genmatrix(x,y)