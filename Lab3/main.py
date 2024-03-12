import sys

from Helper import *
from SolverSMO import SolverSMO

print("Ввод из файла?")
print("1. Да")
print("2. Нет")
input_type = get_int_from_input_min_max(1, 2)

if input_type == 1:
    file = open("input.txt", "r")
    try:
        smo_type, m, n, lambda_, t_obsl = parse_input_string(file.readlines())
    except ValueError as ex:
        print(f"Ошибка при чтении файла: {ex}")
        sys.exit(1)
    file.close()
else:
    print("Выберите тип СМО:")
    print("1. Одноканальная СМО с отказами в обслуживании")
    print("2. Одноканальная СМО с ограниченной очередью")
    print("3. Одноканальная СМО с неограниченной очередью")
    print("4. Многоканальная СМО с отказами в обслуживании")
    print("5. Многоканальная СМО с ограниченной очередью")
    print("6. Многоканальная СМО с неограниченной очередью")
    smo_type = get_int_from_input_min_max(1, 6)

    n = 1
    if smo_type > 3:
        print("Введите количество каналов (n):")
        n = get_int_from_input_min(2)

    m = None
    if smo_type == 2 or smo_type == 5:
        print("Введите количество мест в очереди (m):")
        m = get_int_from_input_min(1)

    print("Введите интенсивность потока (lambla):")
    lambda_ = get_float_from_input(0)

    print("Введите время обслуживания (T_obsl):")
    t_obsl = get_float_from_input(0)

print()
solver = SolverSMO(smo_type, lambda_, t_obsl, m, n)
print(str(solver))
file = open("output.txt", "w")
file.write(str(solver))
file.close()
