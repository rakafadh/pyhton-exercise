import pandas as pd
import matplotlib as mpb
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

meja = pd.read_excel("E:/ITB KEOS/00 - template/medali excel.xlsx")
b = meja["bronze"].value_counts()
s = meja["silver"].value_counts()
g = meja["gold"].value_counts()
wte = pd.ExcelWriter("E:/ITB KEOS/00 - template/tugas 1 pandas/Tabel frekuensi.xlsx")
b.to_excel(wte,"TabelFrekuensiBronze")
s.to_excel(wte,"TabelFrekuensiSilver")
g.to_excel(wte,"TabelFrekuensiGold")
wte.save()
print(b,s,g)

plt.scatter(meja['gold'],meja['total'],color='#ffa500',label='gold')
plt.scatter(meja['silver'],meja['total'],color='#7c757e',label='silver')
plt.scatter(meja['bronze'],meja['total'],color='#783f04',label='bronze')
plt.title("Data Scatter")
plt.show()