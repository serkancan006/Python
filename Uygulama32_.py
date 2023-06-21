tekrar = int(input("Oyunu kaç defa oynamak istiyorsunuz"))
for i in range(1,tekrar+1):
    print("1) DikÜçgen - 2) EşkenarÜçgen - 3) Kare - 4) Dikdöktgen - 5) Daire")
    şekil = input("Hangi Şekli Çizmek istiyorsunuz")
    
    if şekil == "1":
        satir = int(input("Kaç Satir Olsun"))
        for i in range(1,satir+1):
            print("*"*i)
            
    elif şekil == "2":
        satir = int(input("Kaç Satir Olsun"))
        for i in range(1,satir+1):
            print(satir * " " + (2*i-1) * "*")
            satir -= 1

    elif şekil == "3":
        satir = int(input("Kenar sayisi ne olsun"))
        for i in range(1,satir+1):
            for sütun in range(1,satir+1):
                print("*" ,  end=" ")
            print()


    elif şekil == "4":
        satir = int(input("Satir sayisi ne olsun"))
        sütun = int(input("Sütun sayisi ne olsun"))
        for i in range(1,satir+1):
            for j in range(1,sütun+1):
                print("*" ,  end=" ")
            print()
            
    elif şekil == "5":
        satir = int(input("daire satir sayisini giriniz"))
        for sayi in range(satir):
            if sayi > satir/2:
                for k in range(satir-sayi):
                    print(" ",end="")
                for m in range((sayi+2)*2-1):
                    print("*",end="")
                print()
        for sayi in range(satir,0,-1):
            if sayi > satir/2:
                for k in range(satir-sayi):
                    print(" ",end="")
                for m in range((sayi+2)*2-1):
                    print("*",end="")
                print()
    else:
        print("Yanliş seçim yaptiniz")
    