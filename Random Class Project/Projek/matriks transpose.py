'''
NIM/Nama : 16022199/Maharaka Fadhilah
Deskripsi : Program Menentukan Transpose dari sebuah Matriks
Tanggal : 11 September 2022

Kamus : 
baris,kolom = jml baris & kolom dalam int
M = matriks
barisT,kolomT = baris & kolom sesudah di transpose

'''
#Menampilkan judul program
print("====Program Menentukan Matriks Transpose====")
# Algoritma
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))
M = [[0 for j in range(kolom)] for i in range (baris)]


for i in range (baris):
    for j in range (kolom):
        M[i][j] = int(input("Masukkan elemen matriks baris ke-" +str(i+1)+" dan kolom ke-" +str(j+1) + " :  "))
print("==Matriks yg diinput==")
for i in range (baris):
    for j in range(kolom):
        print(str(M[i][j]) + " ", end='')
    print()
print("==Matriks Transpose==")
barisT = kolom
kolomT = baris
MT = [[0 for j in range(kolomT)] for i in range (barisT)]

for i in range (kolomT):
    for j in range (kolomT):
        MT[i][j] = M[j][i]

for i in range (barisT):
    for j in range(kolomT):
        print(str(MT[i][j]) + " ", end='')
    print()

