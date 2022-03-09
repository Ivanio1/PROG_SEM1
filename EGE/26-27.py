f = (open('26-J2.txt'))
N = int(f.readline())
A = []
count=0
for i in range(N):
    A.append(int(f.readline()))
A.sort()
Sred=round(sum(A)/len(A))
Med=A[N//2]
print(Med,Sred)
for i in A:
    if Sred<=Med:
        if Sred<=i<=Med:
            count+=1
    else:
        if Sred >= i >= Med:
            count+=1
print(count)