#FUNCTION
def test_prime(p):
    if (p==1):
        return False
    elif (p==2):
        return True
    else:
        for x in range(2,p):
            if(p % x==0):
                return False
        return True             
print(test_prime(2))
 
# MAIN PROGRAM
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
