f=open('27-10a.txt')
n=int(f.readline())
r=10*10
s=0
for i in range(n):
   a,b,c=map(int,f.readline().split())
   A=[a,b,c]
   m=max(a,b,c)
   s+=m
   for x in A:
       if (m-x)%4!=0 and (m-x)<r:
           r=m-x
print(s,r)
if s%4==0:
    s-=r
print(s)