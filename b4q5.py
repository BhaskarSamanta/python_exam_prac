
n=int(input("enter the numbr of stars you want to print"))
m=n-1

for i in range(0,n+1):
    for j in range(0,m):
            print(end=" ")
    m-=1
    for j in range(0,i+1):
            print("*",end="")
    print("")
        
    
