nin,k=map(int,input().split())
p=list(map(int,input().split()))
v=list(map(int,input().split()))
t=[]
cin=0
for i in range(nin):
    x=v[i]/p[i]
    t.append(x)
while k>=0 and len(t)>0:
    mindex=t.index(max(t))
    if k>=p[mindex]:
        cin=cin+v[mindex]
        k=k-p[mindex]
    p.pop(mindex)
    v.pop(mindex)
    t.pop(mindex)
print(cin)
