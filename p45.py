#hema
nin=input()
if nin==nin[::-1]:
    print("yes")
else:
    value=nin.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=nin.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
