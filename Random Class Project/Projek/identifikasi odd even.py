'''
Maharaka Fadhilah
16022199
Program mengidentifikasi bilangan ganjil dan genap berdasarkan input

Kamus :
a,even,odd = int
'''
#masukkan input
a = int(input("Masukkan bilangan bulat:"))

even = 0
odd = 0 

#Mengidentifikasi bilangan
while a>=0:
    if a % 2 == 0:
        even = even + 1
    elif a == 0:
        even = even + 1
    elif a % 2 != 0:
        odd = odd + 1
    elif int(a) < 0:
        break
    a = int(input("Masukkan bilangan bulat:"))
    
#Tampilkan output 
print("Jumlah bilangan ganjil ada:%s"%(odd))
print("Jumlah bilangan genap ada:%s"%(even))
