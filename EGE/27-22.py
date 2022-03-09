f=open('27-22b.txt')
n=int(f.readline())
x,y=map(int,f.readline().split())
s=[10001]*10
ostx,osty=x%10,y%10
s[ostx]=x
s[osty]=min(s[osty],y)
for i in range(n-1):
    a,b=map(int,f.readline().split())
    A=[10001]*10
    for j in range(10):
        if s[j]!=10001:
            r = s[j] + a
            ostr = r % 10
            A[ostr] = r
    B = [10001]*10
    for j in range(10):
        if s[j] != 10001:
            r = s[j] + b
            ostr = r % 10
            B[ostr] = r
    for j in range(10):
        s[j]=min(A[j],B[j])
print(s[4])