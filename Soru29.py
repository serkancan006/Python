a = int(input('Bir Sayi Giriniz: '))
bol = 2
for i in range(1,a):
    if (a%bol==0):
        print(bol)
        a /= bol
    else:
        bol += 1