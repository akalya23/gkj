a=int(input())
n1=a
d=0
while (a>0):
    b=a%10
    d=d*10+b
    a=a//10
if(n1==d):
    print("yes")
else:
    print("no")
