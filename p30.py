ain=input()
flag=0
for i in range(1,len(ain)):
  j=0
  while j<len(ain) and len(ain[:j]+ain[i+j:])==len(ain)-i:
    n=ain[:j]+ain[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
