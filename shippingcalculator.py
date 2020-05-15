def shipping(n):
    if n == 1:
        return 10.95
    elif n > 1:
        return ((n - 1) * 2.95) + 10.95

n = int(input("enter number of items purchased: "))
print("%.2f" % round(shipping(n),2))


