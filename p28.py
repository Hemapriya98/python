nin=int(input())
m=list(map(int,input().split()))
m.sort()
sin=0
c=0
for i in range(len(m)):
    if m[i]>=sin:
        c=c+1
    sin=sin+m[i]
print(c)
