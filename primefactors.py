n = int(input("enter number. must be 2 or higher: "))


if n >= 2:
    print ("the prime factors of " + str(n) +" are: ")
else:
    print("error. number must be higher than 2.")

while n % 2 == 0:
    print (2)
    n = n // 2
for i in range(3,int(n)):
     while n % i== 0:
        print (i)
        n = n / i
        
