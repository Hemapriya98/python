ain=int(input())
i=0
x=0
b=[]
while i<90 and i<ain:
  r=0
  for j in str(ain-i):
    r+=int(j)
  if r+(ain-i)==ain:
    x+=1
    b.append(ain-i)
  i+=1
print(x)
for i in b:
  print(i)
