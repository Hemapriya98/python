from itertools import permutations
l=list(input())
p = permutations(l)
b=[]
for i in list(p):
    s=''
    for j in i:
       s+=j
    if s not in b:
       b.append(s)
       print(s)
