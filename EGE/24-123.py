f=open('24-1.txt')
s=f.readline()
c=0
cmax=0
for i in range(1,len(s)-1):
    if s[i-1]<s[i]>s[i+1]:
        if c==0:
            c=i
        else:
            cmax=max(i-c,cmax)
            c=i
print(cmax)