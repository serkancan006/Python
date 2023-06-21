a = 0
b = 0

for i in range(1,101):
    b += i
toplamlarinkareleri = b**2 

for i in range(1,101):
    a += i**2

fark = toplamlarinkareleri - a
print('karelerin toplamı: ',a)
print('toplamların kareleri: ',toplamlarinkareleri)
print('fark = ',fark)