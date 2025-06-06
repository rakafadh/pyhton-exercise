num = int(input("Masukkan angka anda= "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if num == sum:
   print(num,"Merupakan sebuah angka Armstrong")
else:
   print(num,"Bukanlah sebuah angka Armstrong")