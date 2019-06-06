lm=int(input())
c=0
for i in range(1,lm):
    if(lm%i==0):
        c+=1
    else:
        continue
if(c==1):
    print("yes")
else:
    print("no") 
