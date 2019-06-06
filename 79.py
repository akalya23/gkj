import math
a,b=map(int,input().split())
c1=a*b
root = math.sqrt(c1)
if int(root + 0.5) ** 2 == c1:
    print("yes")
else:
    print("no")
