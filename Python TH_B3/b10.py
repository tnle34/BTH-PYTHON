import math

def Tinh(R):
    if R < 0:
        return "Bán kính không hợp lệ. Vui lòng nhập một số dương."
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    return f"Chu vi: {chu_vi:.2f}, Diện tích: {dien_tich:.2f}"
R = float(input("Nhập bán kính hình tròn: "))
result = Tinh(R)
print(result)
