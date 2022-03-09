f = (open('26-j6.txt'))
N = int(f.readline())
a=[]
for i in range(N):
    a.append(int(f.readline()))
a.sort()
extra=sum(a)
extraa=int(extra*0.9)
s=0
i=0
a=a[::-1]
while s>extraa:
    a[i]=(a[i]*0.8)
