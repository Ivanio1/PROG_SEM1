f=open('26-39.txt')
N,M=map(int,f.readline().split())
a=[]
b=0
num=0
for i in range(N):
    y=int(f.readline())
    if y>=180 and y<=200:
        b+=y
        num+=1
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
sum-=a[i]
z=s-sum
c=True
j=i-1
pp=len(a)
while c==True and j>=0:
    p=j+1
    while a[p]-a[j]<=z and p<pp:
        p+=1
    if p!=j+1:
        z=z-(a[p-1]-a[j])
        pp=p-1
        j-=1
    else:
        c=False
print(i+num,M-z)




    

