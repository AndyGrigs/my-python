import random
def generate_matrix(rows, cols, min =-10, max = 10):
    matrix = [[random.randint(min, max) for _ in range(cols)] for _ in range(rows)]
    return matrix

# Введення розмірності матриці
rows = int(input("Введіть кількість рядків: "))
cols = int(input("Введіть кількість стовпців: "))

# Генерація матриці
matrix = generate_matrix(rows, cols)
print(matrix)
# Виведення результату
print("Згенерована матриця:")
# print_matrix(matrix)