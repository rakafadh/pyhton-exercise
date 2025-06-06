num = int(input("enter your number: "))
if num < 0:
    print("please input positive number!")
elif num == 0 or num == 1:
    print("please enter number larger than 1")
else:
    fact = 1
    n = num
    while(n > 1):
        fact *= n
        n -= 1 
print("factorial of",num,"is",fact)
