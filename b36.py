lin=[".","~","!","@","#","$","%","^","&","*",":","_","+","-"]
c=0
str1=input()
for i in str1:
    if i in lin:
        c=c+1
print(c)
