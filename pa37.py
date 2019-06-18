n1=int(input())
cin=0
for i in range(n1):
	a,b=map(int,input().split())
	if a<b:
		cin=cin+1
print(cin)
