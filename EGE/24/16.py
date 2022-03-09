mf = [True] * 100
mg = [True] * 100


def F(n):
    if n < 50:
        mf[n] = n
    else:
        if mf[n] == True:
            mf[n] = 2 * G(50 - n // 2)
    return mf[n]


def G(n):
    if n > 40:
        mg[n] = 10
    else:
        if mg[n] == True:
            mg[n] = 30 + F(n + 600 // n)
    return mg[n]


print(F(80))
