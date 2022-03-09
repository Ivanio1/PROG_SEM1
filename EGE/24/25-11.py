def Prostoe(N):
    a=int(N**0.5)
    for i in range(2,a+1):
        if N%i==0:
            return i
    return N

a=[]
for i in range(143146, 143215+1):
    p=Prostoe(i)
    if p!=i :
        if p**5==i:
            print(1,p,p**2,p**3,p**4,p**5,i)
        elif i%(p**2)==0 and Prostoe(i//p**2)==i//p**2:
            m=[1,p,p**2,i//p,i//p**2,i]
            m.sort()
            print(m)
        else:
            b=Prostoe(i//p)
            if i//p==b**2:
                print(1,p,b,i//p,i//b,i)


