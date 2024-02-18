def expanding(numlist):
    count=0
    for i in range(1,len(numlist)-1):
        if int(numlist[i])-int(numlist[i-1])>int(numlist[i+1])-int(numlist[i]):
            count+=1
        else: 
            print('false')
        break 
    if count>0:
        print("true")

user_list=input('enter the values as "," seperated values')
new_list=user_list.split(",")

expanding(new_list)

