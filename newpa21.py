
nin,k=map(int,input().split(" "))
a,b=map(int,input().split(" "))
c,d=map(int,input().split(" "))
if nin==a==c:
	print("yes")
elif k==b==d:
	print("yes")
elif nin==k and a==b and c==d:
	print("yes")
else:
	print("no")
