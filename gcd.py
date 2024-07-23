def gcd(a,b):
    if(a<b):
        (a,b) = (b,a)
    while b:
        (a,b) = (b, (a%b))
    return(a)

result = gcd(14,63)
print(result)