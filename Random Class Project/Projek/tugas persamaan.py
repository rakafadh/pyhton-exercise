import sys
import os
import math

def main():
   # Menampilkan judul program
   print ("Selamat Datang di Program mencari Akar-akar Persamaan Kuadrat")

   # Meminta user memasukkan a b c
   print ("dalam bentuk \nax²+bx+c=0")
   a = int(input("\nMasukkan nilai a: "))
   b = int(input("Masukkan nilai b: "))
   c = int(input("Masukkan nilai c: "))

   # Hitung D
   D = (b*b) - (4*a*c)

   if D < 0:
      print ("akar-akar bilangan tersebut imajiner \n(D<0)")
      sys.exit(1) #exit program

   elif D == 0:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x1 = x2

   else:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x2 = (-b - math.sqrt(D)) / (2*a) 

   # Setelah nilai D dan akar-akar didapat, tampilkan hasil
   print ("\nx1 = %d" %x1)
   print ("x2 = %d" %x2)

   os.system("pause")
if __name__ == "__main__":
   main()