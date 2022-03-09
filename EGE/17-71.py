
c=1000000
n=0
for i in range(1031, 125888+1):
    x=int(i**0.5)
    if i%10!=5 and x**2==i:
        n+=1
        if i%100==36:
            c=min(c,i)
print(n,c)


