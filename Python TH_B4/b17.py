n = int(input("Nhập số n: "))
def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total
print(f"Các số nguyên dương nhỏ hơn {n} có tổng các ước số lớn hơn chính nó là:")
for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i)
