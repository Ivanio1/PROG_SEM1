f=open('27-6b.txt')
n=int(f.readline())
m,m2,m3,m6=0,0,0,0
for i in range(n):
    a=int(f.readline())
    if a%6==0:
        if a>m6:
            if m6>m:
                m=m6
            m6=a
    elif a%2==0:
        m2=max(m2,a)
    elif a%3==0:
        m3=max(m3,a)
    else:
        m=max(a,m)
print(max(m2*m3,m6*max(m,m2,m3)))
