from LinearCongruentialGenerator import *


# Генерирует список случайных чисел при помощи линейного конгруэнтного метода
def generate_numbers(n):
    x0 = 42
    a = 16070093
    b = 453816693
    k = 31
    lcg = LinearCongruentialGenerator(x0, a, b, k)
    result = []
    for _ in range(n):
        random_number = lcg.next()
        result.append(random_number)
    return result


# Получает математическое ожидание, дисперсию и отклонение по списку чисел
def get_mds(lst):
    lst_sum = sum(lst)
    m = lst_sum / len(lst)
    d = 0
    for x in lst:
        d += (x - m) ** 2 / len(lst)
    return m, d, d**0.5


# Получает вероятность попадания числа в диапазон (0.2113; 0.7887)
def get_freq_chance(lst):
    a = 0.5 - (1/12)**0.5
    b = 0.5 + (1/12)**0.5
    c = 0
    for x in lst:
        if a < x < b:
            c += 1
    return c / len(lst)


# Получает вероятность попадания числа в диапазон (0; 0.5)
def get_half_chance(lst):
    a = 0.5
    c = 0
    for x in lst:
        if x < a:
            c += 1
    return c / len(lst)
