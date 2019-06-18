a,b=map(int,input().split())
cin=0
for i in range(a,b+1):
	for j in range(2,i+1):
		if i%j==0:
			break
	if i==j:
		cin=cin+1
print(cin)
