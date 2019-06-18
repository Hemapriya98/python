nin=int(input())
s=input()
lin=["a","e","i","o","u","A","E","I","O","U"]
f=""
for i in s:
	if i not in lin:
		f=f+i
print(f[::-1])
