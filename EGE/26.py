f = (open('26-1.txt'))
a = f.readline()
S,N = map(int,a.split())
S0 = S

A = []
for i in range(N):
    A.append(int(f.readline()))
A.sort()
i = 0
iMax = 0

sum = 0
aMax = 0
while sum<=S:
    sum += A[i]
    i += 1
i=i-1
x=S-(sum-A[i]-A[i-1])
j=i
while A[j]<=x:
    j+=1
print(i,A[j-1])
