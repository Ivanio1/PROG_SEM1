f=open('k8-1.txt')
s=f.readline()
#s='AABCABCABCCCACACACACA'
c=0
cmax=0
b='X'
for i in s:
    if i!=b:
        c+=1
        b=i
        cmax=max(c,cmax)
    else:
        c=1

print(cmax)