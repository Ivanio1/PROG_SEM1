f=open('k8-75.txt')
s=f.readline()
#s='R66666YYY88****000000'
c=0
cmax=0
a=''
b='R'
for i in s:
    if i==b:
        c+=1
        if c>cmax:
            cmax=c
            a=i


    else:
        c=1
        b=i
print(a,cmax)