f=open('28129_B.txt')
s=f.readlines()
a=[]
x1=0
x2=0
for i in range(len(s)):
    a.append(int(s[i]))
#print(a)
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]%160!=a[j]%160:
            if a[i]%7==0 or a[j]%7==0:
                if a[i]+a[j]>x1+x2:
                    x1=a[i]
                    x2=a[j]
print(x1,x2)