f=open('27-35b.txt')
n=int(f.readline())
a=[0,0]
b=[0,0]
c=0
for i in range(n):
    x=int(f.readline())
    if x==0:
        a=[a[0]+a[1],0]
        b=[b[0]+b[1],0]
    elif x%2==0:
        c+=a[0]
        a[1]+=1
    else:
        c+=b[0]
        b[1]+=1
print(c)
