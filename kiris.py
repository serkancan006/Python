L=1
E=210*(10**9)
I=8.333*(10**(-5))
P=0

while P<=10:
    y=-(P*L**3)/(3*E*I)
    P+=0.5
    print("Y değeri:",y)