def Deliteli(x):
    divs = [1, x]
    d = 2
    while d * d <= x:
        if x % d == 0:
            divs.append(d)
            if x // d > d:
                divs.append(x // d)
        d += 1
    return sum(sorted(divs))
print(Deliteli(16))
for i in range(2, 263000+1):
    a=Deliteli(i)
    if Deliteli(a)==i*2:
        print(i)