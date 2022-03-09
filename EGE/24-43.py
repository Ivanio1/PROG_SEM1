f=open('k7-m5.txt')
s=f.readline()
#s='AAACCACCCCACC'
c=0
n=0
s1=''
for i in s:
    if i=='C':
        c+=1
    else:
        if c!=0:
            s1=s1+str(c)+'c'*c
            n+=1
        s1=s1+i
        c=0
if c!=0:
    s1=s1+str(c)+'c'*c
    n+=1

print(n)
print(s[:15],s[-15:])
print(s1[:15],s1[-15:])