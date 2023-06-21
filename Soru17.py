sayi = int(input('bir sayi giriniz: '))
fatma = []
while True:
    if sayi // 2 != 1: 
        fatma.append(sayi % 2)
        sayi = sayi // 2
    else:
        fatma.append(sayi % 2)
        fatma.append(1)
        break
mesaj = ''
for i in fatma[::-1]:
    mesaj += str(i)
    
print(mesaj)
    

