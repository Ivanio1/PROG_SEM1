def F(x):
    n=x//100
    m=x//10%10
    p=x%10
    a=m+n
    b=m+p

    if a>b:
        if b>9:
            return 100000
        else:
            return a*10+b
    else:
        if a > 9:
            return 100000
        else:
            return b * 10 + a
x=100
while F(x)!=43:
    x+=1
print(x)
