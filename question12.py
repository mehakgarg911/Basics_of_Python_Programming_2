def convert(t):
	if(t[-2:] =="AM"):
		if(t[:2]=="12"):
			return "00" + t[2:8]
		else:
			return t[:8]

	if(t[-2:] =="PM"):
		if(t[:2]=="12"):
			return t[:8]

		else:
			temp = int(t[:2])+12
			return str(temp) + t[2:8]
		

time = input("Please input time in 12 hour format (HH:MM:SS AM/PM) : ")
if((len(time)!=11) or (time[-2:]!=("AM" or "PM")) or t[2]!=":" or t[5]!=":" or t[8]!=" " or int(t[:2])<0 or int(t[:2])>12 or int(t[3:5])<0 or int(t[3:5])>60 or int(t[7:9])<0 or int(t[7:9])>60 ):
	print("Please input time in correct format!")

print("24-Hour format : ",convert(time))