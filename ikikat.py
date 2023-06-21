liste = [1, 2, 3, 4, 5, 6, 7]

def ikikat(dizi):
    i = 0
    while i < len(dizi):
        dizi[i] = dizi[i]*2
        i += 1
    return dizi

yeni_liste = ikikat([1, 2, 3, 4, 5, 6, 7])
print (f"Yeni liste: {yeni_liste}")