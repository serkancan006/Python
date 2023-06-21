mail = "mail@gmail.com"
parola = "123"

girilenmail = input("bir mail giriniz")
if girilenmail == mail:
    girilenparola = input("bir parola giriniz")
    if girilenparola == parola:
        print("Giriş yapıldı")
    else:
        print("parola yanlış girildi")
else:
    print("mail yanlis giridi")