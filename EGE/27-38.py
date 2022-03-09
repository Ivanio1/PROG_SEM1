f=open('27-38b.txt')
n=int(f.readline())
s=[0]*10
summ=0
for i in range(n):
    a=int(f.readline())
    s[a]+=1
nmax=0
for i in range(10):
    if s[i]%2!=0:
        nmax=max(nmax,i)
        summ+=(s[i]-1)*i
    else:
        summ+=s[i]*i
print(summ+nmax)
