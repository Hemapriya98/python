new=input()
flag3=0
for i in range(0,len(new)-1):
  for j in range(i+1,len(new)):
    if new[i]<new[j]:
      flag3=1
      print(new[j:])
      break
  if flag3==1:
    break
  else:
    print(new)
