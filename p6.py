nin=int(input())
zin=list(map(int,input().split()))
c=0
for i in range(len(zin)):
    for j in range(i+1,len(zin)):
        for k in range(j+1,len(zin)):
            if zin[i]<zin[j]<zin[k] and i<j<k:
                c=c+1
print(c)
