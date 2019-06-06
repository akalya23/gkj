n2=input()
c=0
l=['a','e','i','o','u','A','E','I','O','U']
for i in n2:
	if i in l:
		c=c+1
		break
if(c>0):
	print('yes')
else:
	print('no')
