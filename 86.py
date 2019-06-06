a2=input().split()
for i in a2:
	s=set(i)
	if len(s) == len(i):
		print("Yes")
	else:
		print("No")
