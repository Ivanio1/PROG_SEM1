f=open('27-5a.txt')
n=int(f.readline())
s=[10**6]*5
x,y=map(int,f.readline().split())
ostx=x%5
osty=y%5
s[ostx]=x
s[osty]=min(s[osty],y)
for i in range(n-1):
    a,b=map(int,f.readline().split())
    A=[0]*5
    for j in range(5):
        A[(a+j)%5]=s[j]+a
    B = [0] * 5
    for j in range(5):
        B[(b + j) % 5] = s[j]+b
    for j in range(5):
        s[j]=min(A[j],B[j])
print(s[0])