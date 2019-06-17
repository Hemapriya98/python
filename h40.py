you=input()
st=0
for i in you:
  st+=int(i)
if str(st)==str(st)[::-1]:
  print("YES")
else:
  print("NO")
