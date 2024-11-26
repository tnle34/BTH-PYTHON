input_string = input("Nhập một câu: ")
count_upper = 0
count_lower = 0
for char in input_string:
    if char.isupper():
        count_upper += 1
    elif char.islower():
        count_lower += 1
print(f"Chữ hoa: {count_upper}")
print(f"Chữ thường: {count_lower}")
