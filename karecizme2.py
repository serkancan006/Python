
satir = int(input("kare satır sayısını giriniz -> "))
for dis in range(1,satir+1):
    if dis == 1 or dis == satir:
        for ic in range(1,satir+1):
             print("*", end=" ")
    else:
        print('*'+((satir*2)-3)*' '+'*',end='')
    print()
    