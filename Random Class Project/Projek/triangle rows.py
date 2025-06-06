
#menyusun * secara increase
rows = int(input("enter your number ="))
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print("\n")
