p,q=map(int,input().split())
input()
Nin=list(map(int,input().split()))
Kin=list(map(int,input().split()))
s=''
for i in Kin:
  Nin.append(i)
  s+=str(max(Nin))+' '
print(s[:-1])
