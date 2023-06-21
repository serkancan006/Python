saniye = int(input('saniyeyi giriniz: '))
saat = saniye // 3600
saniye = saniye % 60
dakika = saniye // 60
saniye = saniye % 60
print("{}sa : {}dk : {}sn".format(saat,dakika,saniye))