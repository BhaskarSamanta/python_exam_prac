arr = []

def binary_search(arr , key ):
    l = 0
    u = len(arr)-1 #10

    while(l<=u):
        
        m = int((l+u)/2) #5
        
        if arr[m] == key:
            return m
        if arr[m] <= key:
            l= m+1
        else:
            u =m-1
    
    return -1

lst = input('Enter The list')
li = [int(x) for x in lst.split()]
user_key =int(input('Enter The Search key: '))
#li = [2,5,7,87,90]

    

result = binary_search(li,user_key)

if result != -1:
    print('The Key is present at index',result)
else:
    print('not Present in List')

    