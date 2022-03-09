def Prostoe(N):
    a=int(N**0.5)
    for i in range(2,a+1):
        if N%i==0:
            return i
    return N
for i in range(106732567, 152673836+1):
    b=int(i**0.25)

    if b**4==i and Prostoe(b)==b:

        print(i,i//b)