#Program mencari luas dibawah kurva
#Maharaka Fadhilah
#16022199

#menampilkan judul program
print("Selamat datang di program mencari luas bawah kurva \n{metode rectangular}")

#kamus 
bawah = int(input('input batas bawah = '))
atas = int(input('input batas atas = '))
n = int(input('input jumlah partisi = '))

#menghitung luas
I = (atas-bawah)/n
L = 0
for i in range(n):
    f = (bawah**2) + 2
    L += f*I
    bawah += I

#hasil
print('Luas Daerah tersebut adalah', (L), 'satuan')