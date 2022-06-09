def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)
output=fact(int(input("enter the number:")))
print(output)