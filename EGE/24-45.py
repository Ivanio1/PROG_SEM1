f=open('k7-m7.txt')
s=f.readline()
#s='AABBCCCABCBACC'
b='C'
s1=''
c=0
r=1
a=0
for i in s:

    if i==b:
        c+=1
    else:
        if c!=0:
            s1='c'*c+s1
            r = r * c
            a+=1
        s1=s1+i
        c=0

if c!=0:
    s1='c'*c+s1
    r = r * c
    a+=1
n=s.count('C')
s1=str(n)+s1[:24]+str(r)+s1[24:35]
#print(str(n)+str(r)+s1)
print(a)
print(s[:35])
print(s1[:35])