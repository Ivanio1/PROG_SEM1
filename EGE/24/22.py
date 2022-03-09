def f(x,y):
    a = 0
    b = 0
    while x * y > 0:
        if x > 0:
            a = a + 1
        if y > 0 and y%7 > b:
            b = y % 7
        x = x // 10
        y = y // 7
    return [a,b]
m=10000000
for x in range(1,10000):
    for y in range(1, 10000):
        if f(x,y)==[4,5]:
            #print(x,y)
            m=min(m,x*y)
            break
print(m)
