def summ(x):
    y=bin(x)
    s=0
    for i in range(2,len(y)):
        s+=int(y[i])
    return s
def F(x):
    s=summ(x)
    y=bin(x)+str(s%2)
    x=int(y,2)
    s = summ(x)
    y = y + str(s % 2)
    return int(y, 2)
n=[]
n.append(222)
for i in range(100):
    A=F(i)
    if A>209 and A<261 and A not in n :
        n.append(A)

print(n,len(n))
