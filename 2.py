yas = input("Yaşınızı Giriniz")
yas = int(yas)

if yas < 14:
    print("merhaba çocuk")
elif 14<= yas < 18:
    print("merhaba genç")
elif 15<= yas < 24:
    print("merhaba üniversiteli")
elif 24<= yas < 30:
    print("evlenme yaşın gelmiş")
elif 30<= yas < 55:
    print("çoluk çocuk nasıl")
elif yas >= 55:
    print("hayatın son demleri")

