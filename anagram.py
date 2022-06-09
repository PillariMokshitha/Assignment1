str1=input("enter the string1:")
str2=input("enter the string2:")
sor1=sorted(str1)
sor2=sorted(str2)

if len(str1)==len(str2):
	if (sor1==sor2):
		print(" given strings are anagram")
	else:
		print(" not anagram")
else:
	print("They are not of equal length")