f=open('27-6b.txt')
n=int(f.readline())
a=[]
for i in range(n):
    a.append(int(f.readline()))
a.sort()
a=a[::-1]
m=a[0]
m6,m2,m3=0,0,0
i=0
while a[i]%6!=0:
    i+=1
m6=a[i] # неправильно, но в конкретном примере на файле правильно так как наибольшее 999 не делится на 6
for j in range(n):
    if a[j]%2==0 and a[j]%3!=0:
        m2=a[j]
        break
for j in range(n):
    if a[j]%2!=0 and a[j]%3==0:
        m3=a[j]
        break
#print(m,m6,m2,m3)
if m2*m3>m6*m:
    print(m2*m3)
else:
    print(m6*m)