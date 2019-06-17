
nin=int(input())
kin=list(map(int,input().split()))
s=[1]*nin
for i in range(nin):
    if i==0:
        if kin[i]>kin[i+1]:
            s[i]=s[i]+s[i+1]
    elif i>0:
        if kin[i]>kin[i-1]:
            s[i]=s[i]+s[i-1]
print(sum(s))
0
