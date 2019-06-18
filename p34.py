X1,Y1=map(int,input().split())
Din=0
List=[]
for i in range(X1):
      List.append(input())
for i in range(X1):
      for j in range(Y1-1):
            if(List[i][j]!='R' and List[i][j+1]!='R'):
                  Din+=3
            elif(List[i][j]!='G' and List[i][j+1]!='G'):
                  Din+=5
print(Din)
