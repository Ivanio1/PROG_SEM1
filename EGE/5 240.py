def perevod(x):
    y=str(x)
    s=''
    s1=''
    for i in range(len(y)):
        t=bin(int(y[i]))[2:]
        while len(t)<4:
            t='0'+t
        s=s+t
    for i in range(len(s)):
        if s[i]=='0':
            s1=s1+'1'
        else:
            s1=s1+'0'
    return int(s1,2)
x=0
while perevod(x)!=151:
    x+=1
print(x,perevod(x))