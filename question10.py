import string

def count(strn):
	lc = 0
	uc = 0
	for i in strn:
		if(i in string.ascii_lowercase):
			lc+=1
		elif(i in string.ascii_uppercase):
			uc+=1
		else:
			pass
	print("Lowercase: ",lc)
	print("Uppercase: ",uc)

strn = input('Please enter a string: ')
count(strn)