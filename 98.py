n2=int(input())
k1=list(map(int,input().split()))
for i in range (0,n1-1):
	if(k1[i]!=i+1):
		print(i)
		break
