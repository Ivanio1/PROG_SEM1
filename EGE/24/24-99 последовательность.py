f=open('24-1.txt')
s=f.readline()
#s='DDAABCDFG'
c=1
cmax=0
b=s[0]
s1=''
for i in range(len(s)-1):
    if s[i]<s[i+1]:
        c+=1
        b+=s[i+1]
        if c>cmax:
            cmax=c
            s1=b
    else:
        c=1
        b = s[i+1]
print(s1)