n2=input()
mid=len(n2)//2
if len(n2)%2!=0:
    for i in range(len(n2)):
        if i==mid:
            print("*",end="")
        else:
            print(n2[i],end="")
else:
    for i in range(len(n2)):
        if i==mid or i==mid-1:
            print("*",end="")
        else:
            print(n2[i],end="")
