nin=int(input())
l=list(map(int,input().split()))
m=[]
ain=1
for i in range(nin-1):
	if l[i]<l[i+1]:
		ain+=1
	else:
		m.append(ain)
		ain=1
m.append(ain)
print(max(m))
