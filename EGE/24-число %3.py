#f=open('24-1.txt')
#s=f.readline()
s='1A13UU1678'
t=''
m=0

for i in s:
    if i>='0' and i<='9':

        t=t+i
        a=t
        while a!='' and int(a)%3!=0:
            a=a[1:]
        if a!='' and int(a)>m:
            m=int(a)


    else:
        t=''
print(m)
