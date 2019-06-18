xin=int(input())
f,sin=0,1
print(sin,end=" ")
for i in range(1,xin):
    c=f+sin
    print(c,end=" ")
    f,sin=sin,c
