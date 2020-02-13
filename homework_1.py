########## 1 TASK ##########
"""Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число
n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел,
записанных через пробел в одну строку.
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4."""

# n = int(input("Введите количество выводимых символов :"))
# list_of_elements = []
# for i in range(n):
#     j = 0
#     while j < i + 1:
#         list_of_elements.append(i + 1)
#         j += 1
#     if j > len(list_of_elements):
#         break
# for elem in list_of_elements[0:n]:
#     print(elem, end=" ")

########## 2 TASK ##########
"""Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки,
 которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" 
(без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения."""

# spis = [int(i) for i in input("Введите элементы списка через пробел: ").split()]
# find = int(input("Введите искомый элемент: "))
# indexes = []
# for i in range(len(spis)):
#     if spis[i] == find:
#         indexes.append(i)
#     else:
#         continue
# if len(indexes) > 0:
#     for index in indexes:
#         print(index, end=" ")
# else:
#     print("Ненаход.")

########## 3 TASK ##########
"""Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению."""
# start_matrix = []
# while True:
#     str_of_elements = input(" Ввести строку элементов: ")
#     if str_of_elements == 'end':
#         break
#     start_matrix.append([int(element) for element in str_of_elements.split()])
#
# result_matrix = [[start_matrix[i - 1][j] + start_matrix[(i + 1) - len(start_matrix)][j] + start_matrix[i][j - 1] +
#                   start_matrix[i][(j + 1) - len(start_matrix[0])] for j in range(len(start_matrix[0]))] for i in
#                  range(len(start_matrix))]
# for i in range(len(start_matrix)):
#     for j in range(len(start_matrix[0])):
#         print(result_matrix[i][j], end=" ")
#     print()

########## 4 TASK ##########
"""Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n2 по спирали, выходящей из левого верхнего
 угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9"""

# n = int(input("Введите размерность матрицы: "))
# matrix = [[0 for j in range(n)] for i in range(n)]
# i, j, k, x = 0, 0, 0, 1
# while x <= n ** 2:
#     matrix[i][j] = x
#     if i != j:
#         matrix[j][i] = (matrix[k][k] + (n - k * 2) * 2) * 2 - 4 - x
#     if j != n - k - 1:
#         j += 1
#     elif i != n - k - 1:
#         i += 1
#     elif x != n ** 2:
#         k += 1
#         i = j = k
#         x = matrix[k][k - 1]
#     x += 1
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j], end=" ")
#     print()
