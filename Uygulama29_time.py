import time
baslangic = time.time()
isim = input('isiminizi giriniz: ')
bitis = time.time() - baslangic
print(f'İsminizi {bitis} sn zamanda girdiniz\nİsminiz = {isim}')