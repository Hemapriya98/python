from operator import xor
from functools import reduce
nin,k=map(int,input().split(" "))
l=[int(x) for x in input().split()]
l1=[]
for i in range(0,k):
	l2=[int(x) for x in input().split()]
	l1.append(l2)
for i in range(0,k):
	gin=l1[i][0]
	rin=l1[i][1]
	t=reduce(xor,l[gin-1:rin])
	print(t)
