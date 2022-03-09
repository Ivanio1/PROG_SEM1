
f=open('26-s1.txt')
N=int(f.readline())
a=[]
b=0
for i in range(N):
    d=int(f.readline())
    if d>100:
        a.append(d)
    else:
        b+=d
a.sort()
w=len(a)//2
A=a[:w]
a=a[w:]
s=0
for x in A:
    s+=0.9*x
if s==int(s):
    s=int(s)
else:
    s=int(s)+1
s=s+sum(a)+b
print(s,A[-1])


