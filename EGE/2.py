print('x','y','z','f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f=(not x or y) and (not y or z)
            if f:
                print(x,y,z,f)
