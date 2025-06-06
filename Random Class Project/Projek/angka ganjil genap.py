from matplotlib.pyplot import pause
import os

num = int(input("masukkan angka: "))

if (num % 2) == 0:
    print(num, "adalah angka genap")
else:
    print(num, "adalah angka ganjil")

os.system("pause")

