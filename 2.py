import random

# Введення розмірів матриці
m = int(input("Введіть кількість рядків матриці (m): "))
n = int(input("Введіть кількість стовпців матриці (n): "))

# Генерація матриці випадкових цілих чисел у діапазоні від -10 до 10
matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]
print("Згенерована матриця:")
for row in matrix:
    print(row)

# Ініціалізація змінних для пошуку стовпчиків
max_negative_col = None
min_positive_col = None
max_negative = float('-inf')
min_positive = float('inf')

# Пошук стовпчиків
for col in range(n):
    for row in range(m):
        if matrix[row][col] < 0 and matrix[row][col] > max_negative:
            max_negative = matrix[row][col]
            max_negative_col = col
        if matrix[row][col] > 0 and matrix[row][col] < min_positive:
            min_positive = matrix[row][col]
            min_positive_col = col

# Заміна стовпчиків, якщо обидва знайдені
if max_negative_col is not None and min_positive_col is not None:
    for row in range(m):
        matrix[row][max_negative_col], matrix[row][min_positive_col] = (
            matrix[row][min_positive_col], matrix[row][max_negative_col]
        )

print("Матриця після заміни стовпчиків:")
for row in matrix:
    print(row)
