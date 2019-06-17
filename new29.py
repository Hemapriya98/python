n1=int(input())
l=list(map(int,input().split()))
pen=[]
for i in range(n1-1):
	for j in range(i,n1):
		c=l[i:j+1]
		pen.append(sum(c))
print(max(pen))
