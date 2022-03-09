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
