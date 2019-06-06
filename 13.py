ni=int(input())
c=0
for i in range(1,ni+1):
  if ni%i==0:
    c+=1
if c==2:
  print("yes")
elif c>2:
  print("no")
