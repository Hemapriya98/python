nin,k=map(int,input().split())
lin=list(map(int,input().split()))
m=0
u=0
q=0
for i in range(len(lin)):
	if lin[i]>m:
		m=lin[i]
while q<k-1:
	u=0
	for i in range(len(lin)):
		if lin[i]>u and lin[i]<m:
			u=lin[i]
			
	m=u
	q+=1
print(m)
