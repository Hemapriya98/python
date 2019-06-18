import sys, string, math
n,kin = map(int,input().split())
k = kin%n
L = list(map(int,input().split()))
L2 = L[-kin:] + L[:-kin]
print(*L2)
