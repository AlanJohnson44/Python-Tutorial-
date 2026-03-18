text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

length = len(text)
if length % 2 == 0:
    mid = length // 2
    first_half = text[:mid]
    second_half = text[mid:]
    
    if first_half == second_half:
        print("Symmetrical: Yes")
    else:
        print("Symmetrical: No")
else:
    print("Symmetrical: No (Length is odd)")
