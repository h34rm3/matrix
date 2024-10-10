m = int(input("Введите количество строк (m): "))
n = int(input("Введите количество столбцов (n): "))


#инициализация матрицы
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Введите элемент [{i+1}][{j+1}]: ")))
    matrix.append(row)

#инициализация матрицы

#обработкаисортировка матрицы
print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(len(matrix)):
    if i % 2 == 0:
        matrix[i].sort()

print("Матрица с отсортированными четными строками:")
for row in matrix:
    print(row)
