nin=int(input())
l=list(map(int,input().split()))
kin=l.copy()
l.sort()
if(kin==l):
    print("yes")
else:
    print("no")
