def Prostoe(N):
    a = int(N ** 0.5)
    for i in range(2, a + 1):
        if N % i == 0:
            return i
    return N
for i in range(35000000,40000000+1):
        j=i
        while j%2==0:
            j=j//2
        p=int(j**0.25)
        if p**4==j and p==Prostoe(p):
            print(i)