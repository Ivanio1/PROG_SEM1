f=open('24 (7).txt')
s=f.readline()
c=4
cmax=0
a=[s[0],s[1],s[2],s[3]]
n=int(len(s))
for i in range(4,n):
    a.append(s[i])
    a=a[1:]
    if a!=['X','Z','Z','Y']:
        c+=1
        cmax=max(c,cmax)
    else:
        c=3
print(cmax)
