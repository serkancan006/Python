n = 0
karar= int(input("sayılar kaça kadar sıralansın?" ))

if karar < 0 :
    while karar < n:
        print(karar,end=' ')
        karar = karar+1
if karar > 0:
    while n <= karar:
        print(n, end=' ')
        n += 1
if karar == 0:
    print(0)

    



