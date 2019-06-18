nin=int(input())
l=[]
cin=0
kr="kabali"
a=sorted(kr)
for i in range(nin):
	s=input()
	l.append(s)
for i in l:
	if sorted(i)==a:
		cin=cin+1
print(cin)
