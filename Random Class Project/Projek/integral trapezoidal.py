#Program mencari luas bawah kurva(2)
#Maharaka Fadhilah
#16022199

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment
# Menampilkan judul program
print("welcome to program mencari luas bawah kurva \n{Metode Trapezoidal}")

# Kamus
a = int(input("input batas bawah : " ))
b = int(input("input batas atas : " ))
n = int(input("input jumlah kotak : " ))

# Mencari luas 
dL = (b - a) / n
Y = a**2 + 2
L = 0

# menampilkan hasil
for i in decimal_range(a, b, dL):
    L += ((i**2+2)+((i+dL)**2+2)*dL)/2
print(f'Nilai luasnya yakni',(L))