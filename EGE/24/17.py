n=0
m=1000000
for i in range(3712, 8432+1):
    if i%2==i%4:
        if i%13==0 or i%14==0 or i%15==0:
            n+=1
            m=min(m,i)
print(n,m)