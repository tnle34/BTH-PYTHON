import math
x, y = 0, 0
while True:
    move = input("Nhập hướng và số bước (ví dụ: UP 5, nhấn Enter để kết thúc): ")
    if not move:
        break

    direction, steps = move.split()
    steps = int(steps)

    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps
distance = round(math.sqrt(x**2 + y**2))
print(f"Khoảng cách từ vị trí hiện tại đến vị trí ban đầu là: {distance}")

