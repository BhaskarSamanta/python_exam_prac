jali_list=[]  
while True:
    choose=input("enter y for yes n for no: ")
    if choose.strip() == "y":
        value=int(input('enter the numbers: '))
        if value == 0:
            jali_list.append(value)
        elif value==1:
            jali_list.append(value)
        else:
            print("enter onely 1 or 0")
    else:
        break
count=0
count2=0
endindex2=0
startindex2=0
for i in jali_list:
    if i==0:
        count+=1
        
    else:
        if count>count2:
            count2=count
            endindex2=jali_list.index(i)
            startindex2=jali_list.index(i)-(count2+1)
            count=0
            continue
        else:
            count=0
            continue
if count2>count:    
    print(f'the vales in the list are {jali_list} and the longest sequence of zero is {count2} the span is {startindex2} and {endindex2}') 
else:
    # endindex2=jali_list.index(i)
    # startindex2=jali_list.index(i)-(count-1)

    print(f'the vales in the list are {jali_list} and the longest sequence of zero is {count} the span is {startindex2} and {endindex2}') 

    