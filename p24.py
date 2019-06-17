nin=int(input())
a=[]
k=bin(2**n1-1)[2::]
lin=len(k)
for i in range(0,2**nin):
	s=bin(i)[2::]
	if len(s)<l:
		a.append([s.count("1"),(lin-len(s))*"0"+s])
	else:
		a.append([s.count("1"),s])
a.sort()
for i in range(0,len(a)):
	print(a[i][1])
