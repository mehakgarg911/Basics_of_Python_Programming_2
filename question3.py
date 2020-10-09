import string

def count(strn):
	lc = 0
	uc = 0
	di = 0
	sy = 0
	for i in strn:
		if(i in string.ascii_lowercase):
			lc+=1
		elif(i in string.ascii_uppercase):
			uc+=1
		elif(i in string.digits):
			di+=1
		else:
			sy+=1
	print("Lowercase: ",lc)
	print("Uppercase: ",uc)
	print("Digits: ",di)
	print("Special Symbols: ",sy)




strn = "P@#yn26at^&i5ve"
count(strn)
