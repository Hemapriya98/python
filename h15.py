xx=int(input())
ain=list(map(int,input().split(" ")))
l=len(ain)
m=[]
for i in range(0,l):
    v=max(ain[i:])
    if(v==ain[i]):
        m.append(v)
for i in range(0,len(m)-1):
    print(m[i],end=" ")
print(m[len(m)-1],end="\n")
print(max(ain),end="")
