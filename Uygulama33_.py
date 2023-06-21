print("1)Iron Man,2)ScarletWitch, 3)CaptainAmerica,4) BlackWidow, 5)Hawkeye,6) AntMan, 7)Falcon,8) Thor,9)Vision,10)Hulk")
print()
sayi = int(input("Yenilmezlerden birini seç "))
if sayi>=1 and sayi<=10:
 sayac=0
 for say in range(sayi+1):
    if sayi<=3:
        sayac+=2
        print(sayac*"*", end="")

    elif sayi>3 and sayi<7:
        sayac+=1
        print(sayac*"*", end="")

    elif sayi>=7:
        print("*", end="")

 print(" yıldız gücünde bir karakter seçtin.")

else:
 print("lütfen yenilmezler listesinden bir tanesinin numarasını giriniz.")