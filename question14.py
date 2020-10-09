
#Dynamically creating class


def acceptstr():
	strn = input("Please enter a string : ")
	return strn

def printstr(strn):
	print(strn)

obj = type("A", (), {"acceptstr": acceptstr,"printstr":printstr})
print(obj)
obj.printstr(obj.acceptstr())


	