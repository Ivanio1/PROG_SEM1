f=open('24-153.txt')
s=f.readline()
#s='AADffD'
c=-1000000
cmin=874497
b='D'
for i in range(len(s)):
    if s[i]==b:
        if i-c+1>2:
            cmin=min(i-c+1,cmin)

        c=i

print(cmin)