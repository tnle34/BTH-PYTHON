input_string = input("Nhập một câu: ")
count_letters = 0
count_digits = 0
for char in input_string:
    if char.isalpha():
        count_letters += 1
    elif char.isdigit():
        count_digits += 1
print(f"Số chữ cái là: {count_letters}")
print(f"Số chữ số là: {count_digits}")
