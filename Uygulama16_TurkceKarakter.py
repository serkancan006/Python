turkcekarakter = ['Ş','ş','Ç','ç','Ğ','ğ','Ö','ö','Ü','ü','İ','ı']

parola = input('Parolanızı Giriniz: ')
for s in parola:
    if s in turkcekarakter:
        print('parolanız türkçe karakter içermemelidir')
        
   
