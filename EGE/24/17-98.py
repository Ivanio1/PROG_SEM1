n=0
m=0
def perevod(x):
    s=[]
    while x!=0:
        a=x%16
        s.append(a)
        x=x//16
    return s
#print(perevod(25))
for i in range(333,11223+1):
    a=perevod(i)
    if a[0]==1 and a[-1]==12 and i%6!=0:
        n+=1
        m=max(i,m)
print(n,m)