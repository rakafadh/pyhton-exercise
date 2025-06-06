num = int(input("masukkan angka: "))

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"bukanlah bilangan prima")
            print(i,"kali",num//i,"adalah",num)
            break
    else:
        print(num,"adalah bilangan prima") 
else:
    print("masukkan angka yang nilainya lebih dari satu!!!")