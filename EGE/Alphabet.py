f=open('inf_26_04_21_24.txt')
cmax=0
S='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1000):
    s=f.readline()
    a=s.count('G')
    if a<25:
        for j in S:
            cmax=max(s.rindex(j)-s.index(j),cmax)
print(cmax)