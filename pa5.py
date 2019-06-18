
r1=input()
r2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
r3 = 0
for i in range(len(r1)):
	if i > 0 and r2[r1[i]] > r2[r1[i - 1]]:
		r3 = r3+ r2[r1[i]] - 2 * r2[r1[i - 1]]
	else:
		r3 = r3+ r2[r1[i]]
print (r3)
