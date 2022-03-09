f=open('26-53.txt')
N = int(f.readline())
a=[]
b=[]
for i in range(N):
    c=int(f.readline())
    if c%2==0:
        a.append(c)
    b.append(c)