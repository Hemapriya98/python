nin=int(input())
l=list(map(int,input().split()))
t=[]
c=0
for i in range(0,nin-2):
	for j in range(i,nin,2):
		c=c+l[j]
	t.append(c)
	c=0
t.sort()
print(t[-1])
