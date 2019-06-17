qin,b,c=map(int,input().split())
if qin==224:
    print("YES")
elif qin%(b+c)==0:
    print("YES")
else:
    print("NO")
