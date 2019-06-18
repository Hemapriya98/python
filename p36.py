import sys,string
jin = int(input())
M = [ int(x) for x in input().split()]
jin = len(M)
cnt = 0
for i in range(0,jin-2) :
    for j in range(i+1, jin-1):
        for k in range(j+1, jin):
            if M[i] > M[j] > M[k] :
                cnt += 1
print(cnt)
