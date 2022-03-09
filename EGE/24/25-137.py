def Prostoe(x):
    p=int(x**0.5)
    for i in range(2,p+1):
        if x%i==0:
            return i
    return x
def Para(x):
    n=0
    d=0
    p=int(x**0.5)
    for i in range(p,1,-1):
        if x//i-i<=90:
            if x%i==0:
                n+=1
                d=x//i
        else:
            if n>=3:
                return d
            else:
                return 0
for i in range(500000, 1000000+1):
    n=Para(i)
    if n!=0:
        print(i,n)

