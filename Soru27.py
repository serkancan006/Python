fatma=int(input("Sayıyı Girin : "))
def asalbul(a):
    if a > 1:
         for i in range(2,a):
              if (a % i) == 0:
                   return 0
         else:
            return a
    else:
         return 0

x = asalbul(fatma) 
y = asalbul(fatma+2)
if x !=0 and y !=0:
    print(fatma,' sayısı Chen Sayıdır')
else:
    print(fatma,' sayısı Chen Sayı değildir')
    
    