f=open('24-1.txt')
s=f.readline()
#s='1A13UU678'
t=0
m=0
s1='0123456789'
for i in s:
    if i>='0' and i<='9': # i in s1:
        a=int(i)
        t=t*10+a
        if t%2!=0 and t>m:
            m=t
    else:
        t=0
print(m)
