nin = int(input())
a = []
if nin%2 == 0:
  for i in range(1,nin):
    if nin%i == 0 and (i==1 or i==2):
      a.append(i)
    elif nin%i == 0 and i%2!=0:
      a.append(i)
else:
  for i in range(1,nin+1):
    if nin%i == 0 and (i==1 or i==2):
      a.append(i)
    elif nin%i == 0 and i%2!=0:
      a.append(i)

print(*a)
