f = (open('26-J1.txt'))
N = int(f.readline())

k=0
A = []
for i in range(N):
    A.append(int(f.readline()))

for i in range(N-1):
    for j in range(i+1,N):
        if A[i]+A[j]==100:
            A[i]=0
            A[j]=0
            k+=1
print(k)