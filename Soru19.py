sayi = int(input('Kaçıncı üçgensel sayıyı istiyorsunuz: '))
while True:
    if sayi<0:
        sayi = int(input('Lütfen pozitif bir sayi giriniz: '))
    else:
        break
fatma = 0
for i in range(1,sayi+1):
    fatma += i
print(sayi,'. Ücgen sayinin degeri : ',fatma,'')

