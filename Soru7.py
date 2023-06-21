import random
a=random.randint(1,100)
print('Tutulan sayı = ',a)
tahmin = int(input('Sayıyı Tahmin Et: '))
skor = 1
while True:
    if tahmin==a:
        print('Tebrikler skorunuz: ',skor)
        break
    if tahmin > 100 or tahmin < 0:
        print('0 ile 100 arasında bir sayi giriniz')
        break
    else:
        skor += 1
        tahmin = int(input('Tutulan Sayıyı Tahmin Et: '))
        
        
