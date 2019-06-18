sin=int(input())
a=""
for i in range(1,sin+1):
	if sin%i==0 and i%2==0:
		a=a+str(i)+" "
print(a.strip())
