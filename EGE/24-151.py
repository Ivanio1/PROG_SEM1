def F(x):
    return x==x[::-1]

f=open('24-j9.txt')
s=f.readline()
c=0
for i in range(len(s)-5):
    if F(s[i:i+5]):
        c+=1
print(c)

