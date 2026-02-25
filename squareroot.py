number = float(input("Enter a number: "))

if number < 0:
    print("Undefined for negative numbers")
else:
    g = number / 2.0
    t = 0.00001
    while abs(g * g - number) > t:
        g = (g + number / g) / 2
        
    print("Square root is approximately:", round(g, 5))
