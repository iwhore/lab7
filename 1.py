import random

# Запитуємо користувача на введення кількості елементів
n = int(input("Введіть кількість елементів у списку (n): "))

# Генеруємо список випадкових цілих чисел у діапазоні від -10 до 10
random_list = [random.randint(-10, 10) for _ in range(n)]
print("Згенерований список:", random_list)

# Знаходимо найбільший від‘ємний елемент
max_negative = None
for num in random_list:
    if num < 0:
        if max_negative is None or num > max_negative:
            max_negative = num

# Формуємо новий список
transformed_list = []
for num in random_list:
    if max_negative is not None and num < max_negative:
        transformed_list.append(num ** 2)  # Квадрат числа
    else:
        transformed_list.append(num)  # Залишаємо без змін

print("Перетворений список:", transformed_list)