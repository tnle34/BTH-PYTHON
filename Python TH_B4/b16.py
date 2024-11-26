input_string = input("Nhập chuỗi các số nhị phân (mỗi số cách nhau bởi dấu phẩy): ")

binary_numbers = input_string.split(',')

print("Các giá trị nhị phân vừa nhập là:")
for binary in binary_numbers:
    print(binary.strip())
