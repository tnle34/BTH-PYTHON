# Nhập một list từ bàn phím, mỗi phần tử cách nhau bởi dấu trống hoặc tab
input_string = input("Nhập danh sách các phần tử (mỗi phần tử cách nhau bởi dấu trống hoặc tab): ")

# Chuyển đổi chuỗi nhập vào thành danh sách các phần tử
my_list = input_string.split()

# In ra danh sách đã nhập
print("Danh sách ban đầu:")
print(my_list)

# Cắt list: lấy list nhưng bỏ phần tử đầu và cuối
if len(my_list) > 2:
    trimmed_list = my_list[1:-1]
else:
    trimmed_list = []
print("Danh sách sau khi cắt bỏ phần tử đầu và cuối:")
print(trimmed_list)

# Thêm phần tử vào list
element_to_add = input("Nhập phần tử muốn thêm vào danh sách: ")
trimmed_list.append(element_to_add)
print("Danh sách sau khi thêm phần tử:")
print(trimmed_list)

# Bỏ phần tử khỏi list
element_to_remove = input("Nhập phần tử muốn bỏ khỏi danh sách: ")
if element_to_remove in trimmed_list:
    trimmed_list.remove(element_to_remove)
    print("Danh sách sau khi bỏ phần tử:")
else:
    print("Phần tử không tồn tại trong danh sách.")
print(trimmed_list)

# Tìm kiếm phần tử trong list
element_to_search = input("Nhập phần tử muốn tìm trong danh sách: ")
if element_to_search in trimmed_list:
    print(f"Phần tử '{element_to_search}' có trong danh sách tại vị trí {trimmed_list.index(element_to_search)}.")
else:
    print(f"Phần tử '{element_to_search}' không tồn tại trong danh sách.")

# Sắp xếp các phần tử trong list
trimmed_list.sort()
print("Danh sách sau khi sắp xếp:")
print(trimmed_list)
