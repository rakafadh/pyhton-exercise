#NIM/Nama: 16022199/Maharaka Fadhilah
#Deskirpsi: Mencari nilai matriks triangular 

#Kamus
# bil = int
# M = matriks

#Menampilkan judul program
print("==Program Mencari nilai Matriks Triangular==")
brs = int(input("Masukan Baris :"))
kol = int(input("Masukan kolom :"))
M = [[0 for i in range (kol)]for j in range (brs)]

#algorithma
for i in range (brs):
    for j in range (kol):
        M[i][j] = int(input(f"Masukan elemen ke-{i},{j} ="))


print("\nMatriks x")
for i in range (brs) :
    for j in range (kol) :
        print(str(M[i][j])+" ", end="")
    print()


c = M[1][0]/M[0][0]
for i in range (1,2) :
    for j in range (kol) :
        M[i][j] = c*M[0][j] - M[1][j]


print("\nMatriks y")
for i in range (brs) :
    for j in range (kol) :
        print(str(M[i][j])+" ", end="")
    print()


c = M[2][0]/M[0][0]
for i in range (2,3) :
    for j in range (kol) :
        M[i][j] = c*M[0][j] - M[2][j]


print("\nMatriks z")
for i in range (brs) :
    for j in range (kol) :
        print(str(M[i][j])+" ", end="")
    print()


c = M[2][1]/M[1][1]
for i in range (2,3) :
    for j in range (kol) :
        M[i][j] = c*M[1][j] - M[2][j]


print("\nMatriks Triangular")
for i in range (brs) :
    for j in range (kol) :
        print(str(M[i][j])+" ", end="")
    print()