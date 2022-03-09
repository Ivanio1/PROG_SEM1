def F(x,y):
    if (y > x):
        z = x
        x = y
        y = z
    a = x
    b = y
    while b > 0:
        r = a % b
        a = b
        b = r
    return [a,x,y]
m=0
for x in range(0,10000):
    for y in range(0,10000):
        r=F(x,y)

        if r[0]==13 and r[1]==65:
            m=max(m,r[2])
print(m)