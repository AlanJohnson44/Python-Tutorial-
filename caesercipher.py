text = input("Enter message: ")
shift = int(input("Enter shift amount: "))
mode = input("Type 'encrypt' or 'decrypt': ")

result = ""

if mode == "decrypt":
    shift = -shift

for char in text:
    if char.isalpha():
        if char.isupper():
            start = 65
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            start = 97
            result += chr((ord(char) - start + shift) % 26 + start)
    else:
        result += char

print("Result:", result)
