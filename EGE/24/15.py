def graf(x,y,A):
    return (y+2*x!=48) or (A<x) or (x<y)
for A in range(1,1000):
    flag=True
    for x in range(1,1000):
        for y in range(1,1000):
            if not graf(x,y,A):
                flag=False
        if not flag:
            break
    if flag==True:
        print(A)