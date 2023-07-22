'''
шахматный модуль.
напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
'''
__all__ = ['check_placement']


def check_placement(list_coordinates: list) -> bool:  # проверка расстановки ферзей
    chess_board = fill_chess_board(list_coordinates)
    '''идея: проверить сколько ферзей стоит на каждой горизонтали и вертикали. если > 1го, то они бью друг друга'''
    # мах кол-во ферзей по горизонталям и диагонялям
    if max(sum(chess_board[i]) for i in range(0, 8)) > 1 or not check_diagonally(chess_board):
        return False

    # транспонируем матрицу и повторяем проверку
    spam_board = [[chess_board[i][j] for i in range(0, 8)] for j in range(0, 8)]  # вспомогательная матрица
    if max(sum(spam_board[i]) for i in range(0, 8)) > 1 or not check_diagonally(spam_board):
        return False

    return True


def fill_chess_board(list_coordinates: list) -> list:  # заполнение доски
    board = list()
    board = [[1 if (i + 1, j + 1) in list_coordinates else 0 for i in range(0, 8)] for j in range(0, 8)]

    return board


def check_diagonally(board: list) -> bool:  # проверка диагоналей
    # кол-во ферзей по диагоналям

    for i in range(6, -1, -1):
        eggs = 0
        for j in range(0, 8 - i):
            eggs += board[i + j][j]
            if eggs > 1:
                return False

    for i in range(0, 6):
        eggs = 0
        for j in range(0, 7 - i):
            eggs += board[j][i + j + 1]
            if eggs > 1:
                return False

    return True


if __name__ == '__main__':
    eggs = [(0, 0), (1, 1), (2, 4), (3, 2), (4, 7), (5, 6), (6, 3), (7, 5)]
    correct_placement = [(0, 0), (1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2)]
    spam = fill_chess_board(eggs)
    for i in spam:
        print(i)

    print(check_placement(eggs))
