def Prostoe(x):
    p=int(x**0.5)
    for i in range(2,p+1):
        if x%i==0:
            return i
    return x
n=0
nmax=0
for i in range(158928, 345293+1):
    p=Prostoe(i)
    if p!=i:
        if p**4==i:
            n+=1
            nmax=max(nmax,i)
print(n,nmax)