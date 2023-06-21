kenar_sayisi = input('Kaç kenarlı kare olsun: ')
kenar_sayisi = int(kenar_sayisi)

for i in range(kenar_sayisi):
    for j in range(kenar_sayisi-1):
        print('*',end=' ')
    print('*')
  