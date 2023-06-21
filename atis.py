import numpy as np
import math
t = 0
v = 50
g = 9.81
liste = []

for t in np.arange (0, 20, 0.5): #artış float olduğu için np.arange kullanıldı
    x= v*math.cos(60*math.pi/180)*t #radyan dereceye çevrildi
    y= v*math.sin(60*math.pi/180)*t - 0.5*g*t*t #radyan dereceye çevrildi
    liste.append (y)
    print(f"Yatayda aldığı yol: {x}\nDüşeyde aldığı yol: {y}\n")
    t+=0.5
print ("Maksimum yükseklik:",max(liste))


