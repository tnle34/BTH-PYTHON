input_string = input("Nhập các từ tiếng Anh, cách nhau bởi dấu cách: ")

words_list = input_string.split()

sorted_words = sorted(words_list)

print("Các từ theo thứ tự từ điển:")
for word in sorted_words:
    print(word)
