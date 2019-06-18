
sin=input()
tin=[]
r=[]
for i in sin:
  if i=='(':
    tin.append(i)
  elif i==')':
    r.append(i)
if len(tin)==len(r):
  print("yes")
else:
  print("no")
