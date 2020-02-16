start_rows = new_rows = int(input("Введите ширину(кол-во строк будущей матрицы): "))
start_columns = new_columns = int(input("Введите длинну(кол-во столбцов будущей матрицы): "))
char_counter = 65

matrix = [[0 for _ in range(start_columns)] for _ in range(start_rows)]


def show_matrix(start_rows, start_columns):
    for i in range(start_rows):
        for j in range(start_columns):
            print(matrix[i][j], end=' ')
        print()


def squares_from_rectangle(start_rows: int, start_columns: int, new_rows: int, new_columns: int, char_counter: int):
    """Showing square segregation in rectangle."""

    if new_columns == new_rows:
        print('Квадрат {} x {}'.format(new_rows, new_columns))
        for i in range(start_rows - new_rows, start_rows):
            for j in range(start_columns - new_columns, start_columns):
                matrix[i][j] = chr(char_counter)
    elif new_rows < new_columns:
        print('Квадрат {0} x {0}'.format(new_rows))
        for i in range(start_rows - new_rows, start_rows):
            for j in range(start_columns - new_columns, start_columns - new_columns + new_rows):
                matrix[i][j] = chr(char_counter)
        if char_counter - 64 == 65:
            char_counter = 65
        else:
            char_counter += 1
        new_columns -= new_rows
        squares_from_rectangle(start_rows, start_columns, new_rows, new_columns, char_counter)

    elif new_rows > new_columns:
        print('Квадрат {0} x {0}'.format(new_columns))
        new_rows -= new_columns
        for i in range(start_rows - new_columns, start_rows):
            for j in range(start_columns - new_columns, start_columns):
                matrix[i][j] = chr(char_counter)
        if char_counter - 64 == 65:
            char_counter = 65
        else:
            char_counter += 1
        start_rows -= new_columns
        squares_from_rectangle(start_rows, start_columns, new_rows, new_columns, char_counter)


squares_from_rectangle(start_rows, start_columns, new_rows, new_columns, char_counter)
show_matrix(start_rows, start_columns)