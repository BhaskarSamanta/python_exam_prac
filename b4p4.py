evoddlist=input("enter the elements of the list:")
temp=[i for i in evoddlist.split(",")]

eve=0
odd=0

for i in range(len(temp)):
    if int(temp[i])%2==0:
        eve+=1
    else:odd+=1

print("the number of the odd values in the list is:",odd)

print("the number of the even values in the list is:",eve)
