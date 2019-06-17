r=input()
r=list(r)
if r==r[::-1]:
	while r==r[::-1]:
		r[-1]=""
h=""
for i in r:
	h=h+i
print(h)
