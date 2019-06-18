nin,rem=map(int,input().split())
p=(nin//2)-1
for i in range(1,p+1):
  if i*p==rem:
    print("yes")
    break
  else:
    p-=1
else:
  print("no")
