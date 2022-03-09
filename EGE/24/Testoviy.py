a={}
for i in range(100806, 100950+1):
    n=0
    for j in range(1,i+1):
        if i%j==0:
            n+=1
            if n>6: break
            a[n]=j
    if n==6:
        print(a[1],a[2],a[3],a[4],a[5],a[6])