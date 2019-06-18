ain,bin=map(int,input().split())
if ain<=bin:
  d=ain2
else:
  d=bin2
m=[]
for i in range(0,d):
  m.append(sorted(list(map(int,input().split()))))
m=sorted(m)
for i in range(0,len(m[0])):
  for j in range(0,len(m)-1):
    if m[j][i]>m[j+1][i]:
      m[j][i],m[j+1][i]=m[j+1][i],m[j][i]
for i in m:
  print(*i)
