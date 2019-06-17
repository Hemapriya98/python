n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in range(0,len(l)):
    if i==l[i]:
        l2.append(l[i])
if len(l2)>0:
    print(*l2)
else:
    print("-1")
