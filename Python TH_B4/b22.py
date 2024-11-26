def all_even_digits(number):
    return all(int(digit) % 2 == 0 for digit in str(number))
even_digit_numbers = [number for number in range(1000, 3001) if all_even_digits(number)]
output_string = ','.join(map(str, even_digit_numbers))
print("Các số có tất cả các chữ số là số chẵn trong khoảng từ 1000 đến 3000 là:")
print(output_string)
