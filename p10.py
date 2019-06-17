Min=int(input())
Nin=list(map(int,input().split()))
s=0
p=[]
for i in range(1,Min):
  p=Nin[:i]
  for j in p:
    if j<Nin[i]:
      s+=j
print(s)
