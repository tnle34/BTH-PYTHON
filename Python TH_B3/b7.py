n = int(input("Nhập số n: "))

def check_even_odd(number):
    if number % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")

check_even_odd(n)
