f=open('27-2b.txt')
n=int(f.readline())
s=[0,0,0]
for i in range(n):
    a, b = map(int, f.readline().split())
    ost=a%3
    A=[0,0,0]
    for j in range(len(s)):
        A[(a+s[j])%3]=max(a+s[j],A[(a+s[j])%3])
    B=[0,0,0]
    ostb=b%3
    for j in range(len(s)):
        B[(b+s[j])%3]=max(b+s[j],B[(b+s[j])%3])
    for j in range(len(s)):
        s[j]=max(A[j],B[j])
print(s[0])