f=open('26-j8.txt')
n=int(f.readline())
S=[]
a=0
b=0
for i in range(n):
    S.append(int(f.readline()))
S.sort()
counta=int(0.7*len(S))
for i in range(counta):
    a+=0.7*S[i]
for i in range(counta,len(S)):
    a+=0.6*S[i]
countb=int(0.5*len(S))
for i in range(countb):
    b+=0.6*S[i]
for i in range(countb,len(S)):
    b+=0.65*S[i]
if a-b>0:
    print(int(a-b),int(S[-1]*0.6))
else:
    print(int(b-a),int(S[-1]*0.65))