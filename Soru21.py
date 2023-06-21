fibo = [1,2]
cift = [1,2]
ekleneceksayi = 0
#FİBO İLK 10 SERİ YAZDIRMA
for i in range (0,31):
    ekleneceksayi = fibo[i]+fibo[i+1]
    if ekleneceksayi < 4000000 and ekleneceksayi % 2 ==0:
        cift.append(ekleneceksayi)
    fibo.append(ekleneceksayi)
print('fibo serisi\n',fibo)
print('fibocift serisi\n',cift)

fibotoplam = 0 
for i in range(0,len(cift)):
    fibotoplam += cift[i]
print('fibocift toplam = ',fibotoplam)