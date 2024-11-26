input_string = input("Nhập danh sách các số (mỗi số cách nhau bởi dấu phẩy): ")
numbers = input_string.split(',')
odd_numbers = [int(num) for num in numbers if int(num) % 2 != 0]
print("Các số lẻ trong danh sách là:")
print(",".join(map(str, odd_numbers)))
