import sys, string, math
n,k1 = map(int,input().split())
k = k1%n
Lin = list(map(int,input().split()))
L2 = Lin[-k1:] + Lin[:-k1]
print(*L2)
