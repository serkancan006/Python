parola = input('parolanızı giriniz: ')
parola_uzunluk = len(parola)
mesaj = 'parolanızın Toplam Uzunluğu = {}'.format(parola_uzunluk)
if parola_uzunluk >12:
    print(mesaj)
    print('parolanız 12 karakteri geçemez')
else:
    print('parola başarıyla oluşturuldu')
