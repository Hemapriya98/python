ipt=int(input())
b=list(map(int,input().split()))
cin=[]
ain=1
for i in b:
  if i not in cin:
    cin.append(i)
for i in range(0,len(cin)-1):
  if cin[i]<cin[i+1]:
    ain+=1
print(ain)
