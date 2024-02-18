words = input('Enetr a string to check: ')

tempStr = words.split(" ")

reverse_str = tempStr[::-1]

k =len(reverse_str)-1

final = ""

for i in reverse_str:
    final += i

    if k>0:

        final += " "
        
    k -= 1
    
print('reversed: ',final)

