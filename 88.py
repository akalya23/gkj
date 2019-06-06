import math
a2,b2=map(int,input().split())
c1=(a2*b2)/math.gcd(a2,b2)
print(int(c1))
