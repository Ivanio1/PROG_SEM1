f=open('26-k2.txt')
N,K=map(int,f.readline().split())
a=[]
for i in range(N):
    a.append(int(f.readline()))
a.sort()
a=a[K:-K]
print(a[-1],sum(a)//len(a))
