pin, qin =[int(i) for i in input().split()]
count =0
for i in range(qin+1):
    k = i*i
    if k in range(pin,qin):
            count+=1
print(count)
