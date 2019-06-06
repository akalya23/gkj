a,c=input("").split()
a=int(a)
b=int(c)
for x in range(a+1,c):
    if(x%2==0):
        continue
    elif(x%2!=0):
        print(x,end=" ")
        
