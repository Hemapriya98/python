import math
nin=int(input())
s=math.radians(nin)
if(s>0 and s<1):
	print(round(math.sin(s),2))
else:
	print(round(math.sin(s)))
