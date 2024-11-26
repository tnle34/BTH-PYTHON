def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

n = int(input("Nhập số n: "))

triangle = pascal_triangle(n)

print(f"{n} dòng đầu tiên của tam giác Pascal:")
for row in triangle:
    print(row)
