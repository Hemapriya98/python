zin=int(input())
y=input().split()
we=len(y)
for j in range(0,we):
	a=y.count(y[j])
	if (a<2):
		print(y[j])
