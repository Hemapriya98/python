N=int(input())
nin=list(map(int,input().split()))
m=max(nin)
a,b=0,0
for i in range(0,len(nin)-1):
  for j in range(i+1,len(nin)):
    if abs(nin[i]+nin[j])<m:
      a,b=nin[i],nin[j]
      m=abs(a+b)
print(a,b)
