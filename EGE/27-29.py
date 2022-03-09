f=open('27-29b.txt')
n=int(f.readline())
r=10**10
rr=10**10
s=0
for i in range(n):
   a,b,c=map(int,f.readline().split())
   A=[a,b,c]
   m=min(a,b,c)
   for x in A:
       if x!=m:
           s+=x
           rr=min(rr,x-m)
       if rr%5!=0:
            r=min(r,rr)
print(s,r)
if s%5==0:
    s-=r
print(s)