full_name = input("Nhập họ và tên: ")

parts = full_name.split()

if len(parts) == 2:
    ho = parts[0]
    ten = parts[1]
    print(f"Họ: {ho}")
    print(f"Tên riêng: {ten}")
else:
    print("Vui lòng nhập đúng định dạng 'Họ Tên'.")
