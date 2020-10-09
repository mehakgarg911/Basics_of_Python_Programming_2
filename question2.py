
def reverse_s(num):  #string style
    newnum = num[::-1]
    return newnum;

def reverse(num):
	newnum = 0
	count = 0
	x=[]
	while(num!=0):
		x.append(num%10)
		num=num//10
		count+=1;


	i = 0;
	while(count!=0):
		newnum+=x[i]*(10**(count-1))
		i+=1
		count-=1
	return newnum


def ifsame(num1,num2):
	if(num1==num2):
		return "SAME"
	else:
		return "NOT SAME"

num=int(input("Enter a number:"))
rnum=reverse(num)
result=ifsame(num,rnum)
print("Result if number is treated as integer: {}".format(result))

num_s=input("Enter a number:")
rnum_s = reverse_s(num_s)
result_s=ifsame(num_s,rnum_s)
print("Result if number is treated as string: {}".format(result_s))
