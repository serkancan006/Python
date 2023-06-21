satir = int(input("daire satır sayısını giriniz"))
for sayi in range(satir):
    if sayi > satir/2:
        for k in range(satir-sayi):
            print(" ", end="")
        for m in range((sayi+2)*2-1):
            print("*", end="")
        print()
for sayi in range(satir, 0, -1):
    if sayi > satir/2:
        for k in range(satir-sayi):
            print(" ", end="")
        for m in range((sayi+2)*2-1):
            print("*", end="")
        print()







