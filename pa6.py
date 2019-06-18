ain,bin=map(str,input().split())
d=0
for x in range(0,len(ain)):
    if((ord(ain[x])-ord(ain[x-1]))!=(ord(bin[x])-ord(bin[x-1]))):
         d=d+1
if(d>0):
      print ("no")
else:
     print ("yes")
