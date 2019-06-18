pin,qin=map(int,input().split())
l=list(map(int,input().split()))
rem=0
for i in range(len(l)):
  if (l[i]==qin):
    rem+=1
    print("Yes")
    break
else:
  print("No")
