f=open('k7b-2.txt')
s=f.readline()

a='DBAC'
c=0
cmax=0
b='D'
for i in range(len(s)):
    if s[i]==b:
        c+=1
        cmax=max(c,cmax)
        if b=='D':
            b='B'
        elif b=='B':
            b='A'
        elif b=='A':
            b='C'
        else:
            b='D'
    else:
        if s[i]=='D':
            c=1
            b='B'
        else:
            c=0
            b='D'
print(cmax)
print(len(s))