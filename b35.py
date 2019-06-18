string=input()
count=0
for i in string:
    if i.isdigit():
        count=count+1
    else:
        pass
print(count)
