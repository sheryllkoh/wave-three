n = int(input("enter number: "))

if n > 1:
    for i in range(2,n):
     if (n%i)==0: 
        print("number is not a prime number")
        break 
    else: 
        print("number is a prime number")
else:
    print("number is not a prime number")
