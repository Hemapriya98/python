nin,min=map(int,input().split())
v=list(map(int,input().split()))
u=0
y=sorted(v)
x=(y[::-1])
for i in range(0,len(x)):
    z = min //(x[i])
    u = u + z
    min = min - (z *x[i])
print(u)
