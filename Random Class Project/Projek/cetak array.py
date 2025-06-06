# Nama/NIM : 16022199/Maharaka Fadhilah
# Deskripsi : Program mencetak isi anggota array

# Kamus :
# n: panjang array; int
# tabel : array

# Algoritma : 
def CetakArray (x,n) :
    for i in range (n) :
        print(f"[{i}] {x[i]}")
    return

print("==Program Mencetak isi Array==")

n = int(input("input jumlah panjang array: "))
tabel = [0 for i in range(n)]
if (n < 0):
    print("Tidak ada Array")
elif(n == 0):
    print("Array kosong")
elif(n > 0):
    for i in range (n) :
        tabel[i] = int(input('Masukkan elemen ke-' + str(i+1) + ': '))
        
CetakArray(tabel,n)
