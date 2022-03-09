def F(x,y,z):
        p=int(x.find(y))
        return x[:p]+z+x[p+len(y):]
s='5'*156

while ('555' in s) or ('333'in s):
    if '555' in s:
        s=F(s,'555','3')
    else:
        s=F(s,'333','5')
print(s)
