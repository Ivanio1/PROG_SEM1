a = [0] * 400
b = [0] * 400
for i in range(399, 0, -1):
    if i >= 36 and i <= 60:
        a[i] = 1
        b[i] = 1
    elif i > 60:
        a[i] = -1
        b[i] = -1
    else:
        p = [a[i + 1], a[i * 2]]
        r = [b[i + 1], b[i * 2]]
        n = [x for x in p if x < 0]
        m = [x for x in r if x > 0]
        if n:
            b[i]=max(n)-1
        else:
            b[i]=max(p)
        if m:
            a[i]=min(m)+1
        else:
            a[i]=min(r)

for i in range(1, 36):
    if a[i]<0:
        a[i]+=1
    else:
        a[i]-=1
    if b[i]<0:
        b[i]+=1
    else:
        b[i]-=1
    print(i, a[i],b[i])
