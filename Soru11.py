sayi = input('Sayıyı Giriniz: ')
basamak = len(sayi)
sayiint = int(sayi)
armstrongsayi=0

for fatma in sayi:
    fatma = int(fatma)
    armstrongsayi += pow(fatma,basamak)
    
if sayiint == armstrongsayi:
    print('Armstrong sayidir')
else:
    print('Armstrong sayi değildir')

