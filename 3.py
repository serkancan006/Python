from posixpath import sep


türkçekarakterler = 'ÜÇŞÖüşçöiİ'
parola = input('parola giriniz')
for harf in parola:
    if harf in türkçekarakterler:
        print('parolada türkçe karakter kullanılmaz')
        