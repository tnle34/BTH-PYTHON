def benefit(t, n, k):
    # Tính lãi suất hàng tháng
    monthly_rate = t / 100
    # Tính số tiền nhận được sau k tháng
    total_amount = n * (1 + monthly_rate) ** k
    return total_amount
# Nhập lãi suất, số vốn ban đầu và số tháng gửi từ bàn phím
t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

# Tính số tiền nhận được sau k tháng
result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")
