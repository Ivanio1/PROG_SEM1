def F1(x):
    if x > 8:
        return 0
    elif x == 8:
        return 1
    else:
        return F1(x + 1) + F1(3 * x) + F1(4 * x)


def F2(x):
    if x > 70:
        return 0
    elif x == 70:
        return 1
    elif x == 35:
        return 0
    else:
        return F2(x + 1) + F2(3 * x) + F2(4 * x)


print(F1(2) * F2(8))
