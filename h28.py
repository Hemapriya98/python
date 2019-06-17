t=input()
lin=list(t)
kin=list(set(list(t)))
p=[]
for i in range(0,len(kin)):
	p.append([lin.index(kin[i]),kin[i]])
p.sort()
f=""
for i in range(0,len(kin)):
	f=f+p[i][1]
print(f)
