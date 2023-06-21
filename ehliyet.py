isim = input ("Lütfen isminizi giriniz... ")
yas = int(input ("Lütfen yaşınızı giriniz... "))
if (yas < 18):
    print (f"{isim}, 18 yaşından küçük olduğun için ehliyet alamazsın...")
else:
    egitim = input ('Lütfen öğrenim durumunuzu giriniz: "İlköğretim", "Ortaöğretim", "Lise", "Lisans", "Yüksek" "Lisans","Doktora"')
    if (egitim == "İlköğretim" or egitim == "Ortaöğretim"):
        print (f"{isim}, Eğitim durumun yetersiz olduğu için ehliyet alamazsın...")
    else:
        print (f"{isim}, Ehliyet alabilirsin...")
