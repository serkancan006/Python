metin1 = input('bir metin giriniz: ')
metin2 = input('bir metin daha giriniz: ')

for char in metin1:
    if char not in metin2:
        print(char)