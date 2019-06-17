n1,k=map(int,input().split())
ain= [[abs(i-k),i]for i in [int(x) for x in input().split()]]
ain.sort()
ain=ain[1:]
ain=[i[1] for i in ain[:3]]
print(*ain)
