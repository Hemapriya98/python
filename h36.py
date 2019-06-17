from itertools import combinations
s=input()
tin=0
l=list(combinations(s,len(s)-1))
for i in range(len(l)):
    if l[i]==l[i][::-1]:
        print("YES")
        tin=1
        break
if tin==0:
    print("NO")
