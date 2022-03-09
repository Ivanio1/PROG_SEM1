s=(9**11*3**20-3**9-27)
base=3
new=''
r=0
while s>0:
    new=str(s%base)+new
    s=s//base
r=new.count('2')
print(r)