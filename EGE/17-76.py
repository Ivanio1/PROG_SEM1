a=int('100000',4)
b=int('1000000',4)
c=0
n=0
def F(x):
    a=[]
    while x!=0:
        a.append(x%10)
        x=x//10
    return a
for i in range(1007,746001+1):
    a=F(i)
    k=a.count(5)
    if max(a)==a[-1] and k%2==0 and k>=2:
        n+=1
        if a[-1]==5 and a[-2]==0:
            c=max(c,i)
print(n,c)


