ain=int(input())
f=0
for i in range(2,ain):
	if ain%i==0:
		f=1
print("yes" if f==1 else "no")
