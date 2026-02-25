num = int(input("Enter a number to check: "))
str_num = str(num)
power = len(str_num)
sum_digits = 0

for digit in str_num:
    sum_digits = sum_digits + int(digit) ** power

if num == sum_digits:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
