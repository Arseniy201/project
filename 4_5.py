from functools import reduce
def my_f(el_1, el_2):
    return el_1*el_2

print(f'Список четных значений{[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Результат перемножения{reduce(my_f, [el for el in range(99, 1001) if el % 2 == 0])}')