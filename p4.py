ain,b=map(str,input().split())
#d=len(ain)-len(b)
#d=abs(d)
d=0
if len(ain)>len(b):
    mins=b
    maxs=ain
elif len(ain)<len(b):
    mins=ain
    maxs=b
else:
    mins=ain
    maxs=b
for i in range(0,len(mins)):
    if ain[i]==b[i]:
        continue
    else:
        d=d+abs(ord(a1[i])-ord(b[i]))
while(i+1<len(maxs)):
    d=d+ord(maxs[i+1])-96
    i=i+1
print(d)
