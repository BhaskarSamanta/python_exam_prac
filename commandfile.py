import sys

n=sys.argv[1]
m=sys.argv[2]

with open(n,'rb') as first, open(m,'wb') as second:
    for i in first:
        second.write(i)
    print("the txt files are copyed")
