
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

full_string = string1 + " " + string2
print("Concatenated String:", full_string)

print("Total length of string is:", len(full_string))

print("Enter the range for the sub-string (start and end index):")
start_index = int(input("Start index: "))
end_index = int(input("End index: "))

sub_string = full_string[start_index:end_index]
print("Extracted Sub-string:", sub_string)
