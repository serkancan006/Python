for sayi in range(1,100):
    if sayi%5 ==0 and sayi%3 ==0:
        print("FizzzzzBuzzzz",end="-")
    elif sayi % 3 == 0:
        print("Fizz",end="-")
    elif (sayi % 5 ==0):
        print("Buzz",end="-")
    
    else: print(sayi,end="-")
