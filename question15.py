class A:
	def getstring(self):
		strn = input("Please enter a string: ")
		return strn
	def printstring(self,strn):
		print(strn.upper())

objA = A()
print(objA)
strn = objA.getstring()
objA.printstring(strn)
			
