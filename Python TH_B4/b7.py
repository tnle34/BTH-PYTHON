input_string = input("Nhập một chuỗi: ")

filtered_string = ''.join([char for char in input_string if not char.isdigit()])

print("Chuỗi mới sau khi loại bỏ các chữ số là:")
print(filtered_string)
