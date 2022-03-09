f=open('27-1b.txt')
n=int(f.readline())
s=0
r=10000
for i in range(n):
    a,b=map(int,f.readline().split())
    s+=min(a,b)
    raznost=abs(a-b)
    if raznost%3!=0:
        r=min(r,raznost)
if s%3==0:
    s+=r
print(s)