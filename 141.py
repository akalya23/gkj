n=input()
m=[]
n=n.split()
a=int(n[0])
d=int(n[1])
for i in range(a+1,d):
    if(i%2!=0):
        m.append(str(i))
c=' '.join(m)
print(c)
        
