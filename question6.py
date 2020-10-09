import string

def checkvalid(strn):
	lc = 0
	uc = 0
	di = 0
	sy = 0
	
	if(len(strn)>=6 and len(strn)<=16):
		for i in strn:
			if(i in string.ascii_lowercase):
				lc+=1
			elif(i in string.ascii_uppercase):
				uc+=1
			elif(i in string.digits):
				di+=1
			elif(i in ('$','#','@')):
				sy+=1
			else:
				pass

			if(lc>0 and uc>0 and di>0 and sy>0):
				return "It is a valid password";
			else:
				pass

		if(lc==0):
			return "Password should contain atleast 1 letter between [a-z]!"
		if(uc==0):
			return "Password should contain atleast 1 letter between [A-Z]!"
		if(di==0):
			return "Password should contain atleast 1 number between [0-9]!"
		if(sy==0):
			return "Password should contain atleast 1 character from [$#@]!"

	else:
		return "Password length not in range of 6-16!"


strn = "bdeu"
c = checkvalid(strn)
print(c)

	