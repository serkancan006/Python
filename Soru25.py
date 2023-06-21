sayi = int(input('Bir Sayi Giriniz: '))
tambolenler = []
for i in range(1,sayi+1):
    if sayi % i == 0:
        tambolenler.append(i)
tambolensayisi = len(tambolenler)
if sayi % tambolensayisi == 0:
    print(sayi,' sayisi Tau Sayisidir')
else:
      print(sayi,' sayisi Tau Sayisi Degildir')
      
      