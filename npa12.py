import sys, string, math
n,k1 = map(int,input().split())
k = k1%n
L = list(map(int,input().split()))
L2 = L[-k1:] + L[:-k1]
print(*L2)
