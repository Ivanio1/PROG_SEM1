f=open('27-15b.txt')
n=int(f.readline())
a=[0]*14
s=[]
rez=0
for i in range(5):
    s.append(int(f.readline()))
for i in range(n-5):
    a[s[0]%14]+=1
    x=int(f.readline())
    s.append(x)
    s=s[1:]
    if x%14==0:
        rez+=a[0]
    else:
        rez+=a[14-(x%14)]
print(rez)