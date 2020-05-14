import math 

def hypotenuse(length_a, length_b):
    return (math.sqrt(length_a ** 2 + length_b **2))

a = int(input("enter A value: "))
b = int(input("enter B value: "))

print("the length of the hypotenuse is ", hypotenuse(a,b))