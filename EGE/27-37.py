f=open('27-37a.txt')
n=int(f.readline())
c=0
a=[]
for i in range(n):
    a.append(int(f.readline()))
for i in range(n-1):
    for j in range(i+2,n):
        if a[i]+a[i+1]==a[j]:
            c+=1
print(c)
