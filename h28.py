t=input()
l=list(t)
k=list(set(list(t)))
p=[]
for i in range(0,len(k)):
	p.append([l.index(k[i]),k[i]])
p.sort()
f=""
for i in range(0,len(k)):
	f=f+p[i][1]
print(f)
