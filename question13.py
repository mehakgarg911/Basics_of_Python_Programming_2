import random
import string

def genrandom(strn):

	ranstring = ""
	length = len(strn)
	count = 0
	while(ranstring!=strn):
		ranstring = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k = length))
		print(ranstring)
		count+=1

	print("{} generated after {} iterations.".format(ranstring,count))

strn = "JK"
genrandom(strn)

