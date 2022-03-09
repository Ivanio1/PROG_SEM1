f=open('27991_B (1).txt')
n=int(f.readline())
a=[]
x1,x2=0,0
for i in range(n):
    a.append(int(f.readline()))
#print(a)
for i in range(n-1):
    for j in range(i+1,n):
        if abs(a[i]-a[j])%2==0:
            if a[i]%17==0 or a[j]%17==0:
                if a[i]+a[j]>x1+x2:
                    x1=a[i]
                    x2=a[j]
print(x1,x2)