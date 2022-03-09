f=open('27-21b.txt')
n=int(f.readline())
s=[False]*10
x,y=map(int,f.readline().split())
s[x%10]=x
s[y%10]=max(s[y%10],y)
for i in range(n-1):
    a,b=map(int,f.readline().split())
    A=[0]*10
    for j in range(10):
        if s[j]!=False:
            r=s[j]+a
            ostr=r%10
            A[ostr]=r
    B = [0] * 10
    for j in range(10):
        if s[j] != False:
            r = s[j] + b
            ostr = r % 10
            B[ostr] = r
    for j in range(10):
        s[j]=max(A[j],B[j])
print(s)