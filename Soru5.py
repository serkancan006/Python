m = ''
for i in range(2,10):
    m += "\nFatmanın {}'leri\n".format(i)
    for a in range(0,100,i):
            m += str(a)+'--' 
print(m)
