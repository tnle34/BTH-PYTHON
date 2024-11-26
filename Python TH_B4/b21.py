# Nhập chuỗi các số nhị phân từ bàn phím, phân tách bởi dấu phẩy
input_string = input("Nhập chuỗi các số nhị phân (mỗi số cách nhau bởi dấu phẩy): ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# Kiểm tra các số nhị phân có chia hết cho 5 hay không
divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]

# In ra các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy
output_string = ','.join(divisible_by_5)
print("Các số nhị phân chia hết cho 5 là:")
print(output_string)
