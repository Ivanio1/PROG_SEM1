f=open('test.txt')
N,M=map(int,f.readline().split())
a=[]
b=0
for i in range(N):
    y=int(f.readline())
    if y>=180 and y<=200:
        b+=y
    else:
        a.append(y)
a.sort()

s=M-b
sum = 0
i=0
while sum<=s:
    sum += a[i]
    i += 1
i=i-1
w=0
count=0
while i>0:
    result=w+a[i]
    if result<=s:
        i-=1
        w+=a[i]
    count+=1
print()


    

