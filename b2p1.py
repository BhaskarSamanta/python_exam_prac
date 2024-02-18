list1=input("enter the items of 1st list as comma seperetade values")
list2=input("enter the items of 2nd list as comma seperated values")

temp1=list1.split(",")
temp2=list2.split(",")

for i in temp1:
    for j in temp2:
        if int(i)==int(j):
            print("true")
            break
        else:
            print('false') 
            continue    

            


