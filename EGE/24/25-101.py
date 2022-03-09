def Prostoe(x):
    a=int(x**0.5)
    for i in range(2,a+1):
        if x%i==0:
            return i
    return x
n=0
nmax=0
for i in range(125697,190234+1):
    p=Prostoe(i)
    if i!=p:
        if i%p==0 and i//p==Prostoe(i//p) and i//p!=p:
            n += 1
            nmax = max(nmax, i)
print(n,nmax)
