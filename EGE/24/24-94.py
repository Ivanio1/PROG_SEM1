#f=open('24-1.txt')
#s=f.readline()
s='AABCBDFGKL'
c=0
cmax=0
b='W'
for i in s:
    if i > b:
        c+=1
        cmax=max(c,cmax)

    else:
        c=1
    b = i
print(cmax)