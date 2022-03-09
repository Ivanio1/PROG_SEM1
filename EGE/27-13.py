f=open('27-13b.txt')
N=int(f.readline())
k,k2,k7,k14=0,0,0,0
a=[]
rez=0
for i in range(7):
    a.append(int(f.readline()))
for i in range(N-7):
    k+=1
    if a[0]%2==0:
        k2+=1
        if a[0]%7==0:
            k7+=1
            k14+=1
    elif a[0]%7==0:
        k7+=1
    x=int(f.readline())
    a=a[1:]
    a.append(x)
    if x%2==0:
        if x%7==0:
            rez+=k
        else:
            rez+=k7
    elif x%7==0:
        rez+=k2
    else:
        rez+=k14
print(rez)