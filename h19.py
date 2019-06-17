nin,k=map(int,input().split())
din=[]
for i in range(nin):
	s1=set(map(int,input().split()))
	din.append(s1)
c=s1.intersection(*din)
print(*c)
