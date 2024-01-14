import random
import numpy as np


def input_array_1():
    array_1 = None
    array_2 = None
    input_type = input("\nВыберите тип ввода данных:\n"
                       "1. вручную\n"
                       "2. сгенерировать случайным образом\nВведите тип ввода данных: ")
    if input_type == '1':
        if input_type == '1':
            array_1 = np.array([int(x) for x in input("Введите первый массив чисел через пробел: ").split()])
            array_2 = np.array([int(x) for x in input("Введите второй массив чисел через пробел: ").split()])

    elif input_type == '2':
        n = int(input("Введите длину массивов: "))
        array_1 = np.array([random.randint(0, 100) for _ in range(n)])
        array_2 = np.array([random.randint(0, 100) for _ in range(n)])
        print("Первый массив:", array_1)
        print("Второй массив:", array_2)


    else:
        print("Неверный тип ввода данных")
        array_1 = None
        array_2 = None

    return array_1, array_2


def task_1(array_1, array_2):
    try:
        array_1.sort(reverse=True)
        array_2.sort()
        array_sum = []
        for i in range(len(array_1)):
            if array_1[i] == array_2[i]:
                array_sum.append(0)
            else:
                array_sum.append(array_1[i] + array_2[i])

        array_sum.sort()
        return array_sum
    except IndexError:
        print("Массивы разной длины")
        return None

