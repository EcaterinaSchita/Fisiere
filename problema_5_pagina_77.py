vocale='aseytujyrdfkyluoikjumynhbtrdb'
x=0
with open ('c:/User/user/Desktop/python.txt', 'r' ) as f:
    b=f.read()

with open('python.txt', 'w') as f:
    for a in b:
        if a in vocale:
            f.write(a)
            x=+1
print('Vocalele sirului sunt:', x)            