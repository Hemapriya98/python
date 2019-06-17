ain,bin =map(str,input().split())
c = 0
c+=abs(len(bin)-len(ain))
if(len(ain)<=len(bin)):
	max = bin
	min = ain
else:
	max = ain
	min = bin
for i in range(len(min)):
	if(min[i]!=max[i]):
		c+=1
print(c)
