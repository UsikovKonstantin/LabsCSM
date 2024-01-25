from pulp import LpVariable, LpProblem, LpMaximize, value
import time

# Объявление переменных
x1 = LpVariable("x1", lowBound=0, cat="Integer")
x2 = LpVariable("x2", lowBound=0, cat="Integer")

# Добавление целевой функции
problem = LpProblem("0", LpMaximize)
problem += 6 * x1 + 8 * x2, "Целевая функция"

# Добавление ограничений
problem += 2 * x1 + x2 <= 400, "1"
problem += x1 + 3 * x2 <= 600, "2"
problem += 4 * x1 + 5 * x2 <= 1238, "3"

# Решаем задачу и замеряем время
start = time.time()
problem.solve()
stop = time.time()

print("Прибыль:")
print(value(problem.objective), "\n")

print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", int(variable.varValue))
print()

print("Время :")
print(1000 * (stop - start), "мс")
