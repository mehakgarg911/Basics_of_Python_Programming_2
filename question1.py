def product(x,y):
	p=x*y
	if(p<=1000):
		return p
	else:
		return x+y

print(product(100,200))