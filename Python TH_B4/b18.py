n = int(input("Nhập số nguyên n: "))
def fibonacci_less_than(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
fib_list = fibonacci_less_than(n)
print(f"Các số Fibonacci nhỏ hơn {n} là:")
print(fib_list)
