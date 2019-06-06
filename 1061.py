n1,k=map(int,input().split())
l=list(map(int,input().split()))
a1=[]
for i in range(len(l)):
	if(l[i]%2!=0):
		a1.append(l[i])
print(a1[k-1])
