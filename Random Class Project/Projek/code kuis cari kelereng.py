print("{=Selamat datang di program menghitung harga kelereng=}")

m = int(input("berapa kelereng merah yg anda beli? = "))
h = int(input("berapa kelereng hijau yg anda beli? = "))
k = int(input("berapa kelereng kuning yg anda beli = "))
x = m*1000
y = h*1500
z = k*2000
bilangan = int(k)
jumlah_nol = 0
total4 = (x+y+z)
print(total4)

if (m % 3) == 0:
    total = ((x-200*m)+y+z)
    print("harganya", total)
elif (h % 4) == 0:
    total2 = ((x+(y-400*h)+z))
    print("harganya", total2)
else:
    for i in range(2, bilangan+1):
        if bilangan % i == 0:
            stat = 1
            jumlah_nol = jumlah_nol+stat
    if jumlah_nol == 1:
        total3 = (x+y+(z-500*k))
        print(total3)



    



    
    


