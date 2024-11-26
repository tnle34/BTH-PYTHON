input_string = input("Nhập dãy các từ (mỗi từ cách nhau bởi dấu trống hoặc tab): ")

words = input_string.split()

max_length = max(len(word) for word in words)

longest_words = [word for word in words if len(word) == max_length]

print("Từ dài nhất trong dãy vừa nhập là:")
for word in longest_words:
    print(word)
