sin=input()
ka=""
lin=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in sin:
	for j in range(0,len(lin)):
		if i==lin[j]:
			ka=ka+lin[(j+3)%26]
		elif i==lin[j].lower():
			ka=ka+lin[(j+3)%26].lower()
print(ka)
