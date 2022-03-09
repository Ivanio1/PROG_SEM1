
def perevod(x):
    s=''
    while x!=0:
        a=str(x%4)
        s=a+s
        x=x//4
    return int(s)
print(perevod(100))