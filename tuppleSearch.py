squares = []
i=1
while(i<=10):
    squares.append(i**2)
    i+=1
flag = True
i=0
while(flag):
    if(squares[i]==9):
        print(i)
        flag = False
    i+=1    
