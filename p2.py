from itertools import combinations
sin,num=map(str,input().split())
num=int(num)
sin=list(sin)
p=list(combinations(sin,len(sin)-num))
d=min(p)
lin=""
for i in d:
    lin=lin+i
    
print(lin)
