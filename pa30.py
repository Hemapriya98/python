nin,m,l=input().split()
cin=0
for i,j in zip (nin,m):
    if(i!=j):
        cin+=1
if(cin==int(l)):
    print("yes")
else:
    print("no")
