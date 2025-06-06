bilangan_awal=int(input("masukan ujung selang awal : "))
bilangan_akhir=int(input("masukan ujung selang akhir : "))
banyak_bilangan_prima=0
bilangan_prima_terbesar=0

for i in range(bilangan_awal,bilangan_akhir+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
               break
            else:
                banyak_bilangan_prima+=1
                bilangan_prima_terbesar=j-1
            
if(banyak_bilangan_prima == 0) or (bilangan_prima_terbesar==0):
    print("tidak ada bilangan prima pada selang " ,bilangan_awal, bilangan_akhir)
else:
    print("banyak nya bilangan pada selang tersebut : ", banyak_bilangan_prima , "bilangan prima terbesar adalah", bilangan_prima_terbesar)