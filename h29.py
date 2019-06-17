get=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(get-1):
	for j in range(i,get):
		c=l[i:j+1]
		p.append(sum(c))
print(max(p))
