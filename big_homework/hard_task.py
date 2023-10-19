def input_matrix(size: int) -> list[list[int]]:
    """Функция для ввода матрицы"""
    matrix = []
    print(f"Введите матрицу размером {size}x{size}: ")
    for i in range(size):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def sum_in_row(matrix: list[list[int]], row_index: int) -> int:
    """Подсчет суммы в строке"""
    return sum(matrix[row_index])

def sum_in_column(matrix: list[list[int]], column_index: int) -> int:
    """Подсчет суммы в столбце"""
    return sum(matrix[row_index][column_index] for row_index in range(len(matrix)))

def sum_in_main_diag(matrix: list[list[int]]) -> int:
    """Подсчет суммы на главной диагонали"""
    return sum(matrix[i][i] for i in range(len(matrix)))

def sum_in_additional_diag(matrix: list[list[int]]) -> int:
    """Подсчет суммы на побочной диагонали"""
    return sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))

def check_rows(matrix: list[list[int]], check: int) -> bool:
    """Функция возвращает True, если все строки матрицы в равны"""
    for i in range(len(matrix)):
        if sum_in_row(matrix, i) != check:
            return False

    return True

def check_columns(matrix: list[list[int]], check: int) -> bool:
    """Функция возвращает True, если все столбцы матрицы в равны"""
    for i in range(len(matrix)):
        if sum_in_column(matrix, i) != check:
            return False

    return True

def is_magic(matrix: list[list[int]]) -> bool:
    """Функция возвращает True, если суммы всех строк, столбцов и диагоналей равны"""
    magic_sum = sum_in_main_diag(matrix)
    return (magic_sum == sum_in_additional_diag(matrix)
            and check_rows(matrix, magic_sum)
            and check_columns(matrix, magic_sum))


def test():
    assert is_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]])


if __name__ == '__main__':
    size = int(input("Введите размер массива: "))
    matrix = input_matrix(size)
    print(is_magic(matrix))
