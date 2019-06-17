nin,k=map(int,input().split())
lin=list(map(int,input().split()))
for i in range(k):
	u,v=map(int,input().split())
	c=lin[u-1:v]
	print(sum(c))
