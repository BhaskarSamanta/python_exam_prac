d=[{'name':'Ram','phone':'9434141414','email':'ram@gmail.com'},
   {'name':'laksman','phone':'8434151515'},
   {'name':'bharat','phone':'9434161416','email':'bharat@gmail.com'},
   {'name':'satrughna','phone':'6434171717','email':'satrughna@gmail.com'}]
a=d[0].get('name')

for i in range(len(d)):
    my_str = d[i].get('phone')
    if my_str.endswith('5'):
        print('whose phone number ends with 5',d[i].get('name'))
for i in range(len(d)):
    my_str = d[i].get('email')
    if my_str == None:
        print ("the user whop has no email",d[i].get('name'))
for i in range(len(d)):
    my_str = d[i].get('phone')
    if my_str.startswith('9'):
        print('whose phone number starts with 9',d[i].get('name'))
        


