n=15
a = [-1] * (3 * n + 2)
def F1(x):
    if a[x]<0:
        a[x]=F1(x+1)+F1(x+2)+F1(3*x)
    return a[x]
def G(x,y):
    for i in range(3*n+2):
        a[i]=-1
    a[y]=1
    for i in range(y+1,3*n+2):
        a[i]=0
    return F1(x)
print(G(2,4)*G(4,11)*G(11,15))