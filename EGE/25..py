def Prostoe(N):
    a=int(N**0.5)
    for i in range(2,a+1):
        if N%i==0:
            return i
    return N
def Razlogenie(x):
    a=[]
    while x!=1:
        p=Prostoe(x)
        a.append(p)
        x=x//p
    return a
print(Razlogenie(130321))
def Kolichestvo(x):
    a=Razlogenie(x)
    c=1
    k=1
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            k+=1
        else:
            c=c*(k+1)
            k=1
    c=c*(k+1)
    return c
print(Kolichestvo(8))
def Deliteli(x):
    a=[]
    for i in range(1,x//2+1):
        if x%i==0 and x//i>i:
            a.append(i)
            a.append(x//i)
    a.sort()
    return a
print(Deliteli(8))
