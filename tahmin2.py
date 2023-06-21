from random import randint
kolaySeviyeHak = 10
zorSeviyeHak = 5
#Tahmini kontrol eden fonksiyon
def tahminKontrol (seninTahminin, bilgisayarTuttu, hak):
 if seninTahminin > bilgisayarTuttu:
    print ("Bir dahakine küçük bir sayı tahmin et!")
    return hak - 1
 elif seninTahminin < bilgisayarTuttu:
    print ("Bir dahakine büyük bir sayı tahmin et!")
    return hak - 1
 else:
    print ("Tabrikler, kazandın!")
    
#zorluk seviyesini ayarlayan bir fonksiyon yaz.
def zorlukSeviyesi ():
 seviye = input ('Zorluk seviyesini seçin: "zor", "kolay')
 if seviye == "zor":
    print ("5 tahmin hakkın var.")
    return zorSeviyeHak
 else:
    print ("10 tahmin hakkın var.")
    return kolaySeviyeHak

def tahminOyunu ():
 #1 ile 100 arasında rastgele bir sayı seçtir.
 print ("Bilgisayar 1-100 arasında bir sayı seçti.")
 bilgisayarTuttu = randint (1, 100)
 hak = zorlukSeviyesi ()
 #hakkı bitene kadar oyun devam etsin.
 seninTahminin = 0
 
 while seninTahminin != bilgisayarTuttu:
    #Tahmin yanlışsa hakkı bir düşsün
    print (f"kalan tahmin hakkın {hak}")

    #Kullanıcıdan bilgisayarın tuttuğu sayıyı tahmin etmesini iste
    seninTahminin = int (input ("Sence bu sayı nedir?"))
    hak = tahminKontrol (seninTahminin, bilgisayarTuttu, hak)
    if hak == 0:
        print ("Tahmin hakkın bitti, oyunu kaybettin!")
        return
tahminOyunu () 