def GCD(a,b):
    rem=a%b
    if rem==0:
        return b 
    else:
        return GCD(b,rem)

ans=GCD(15,12)    
print(ans)
