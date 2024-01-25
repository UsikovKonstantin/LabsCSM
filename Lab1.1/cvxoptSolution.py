from cvxopt.modeling import variable, op
import time

# Объявление переменных
x = variable(2, "x")

# Целевая функция
f = - (6 * x[0] + 8 * x[1])

# Ограничения
cons1 = (2 * x[0] + x[1] <= 400)
cons2 = (x[0] + 3 * x[1] <= 600)
cons3 = (4 * x[0] + 5 * x[1] <= 1238)
cons4 = (x >= 0)

# Создаем задачу
problem = op(f, [cons1, cons2, cons3, cons4])

# Решаем задачу и замеряем время
start = time.time()
problem.solve(solver='glpk')
stop = time.time()

print("\nПрибыль:")
print(abs(problem.objective.value()[0]), "\n")

print("Результат:")
print(int(x.value[0]))
print(int(x.value[1]), "\n")

print("Время:")
print(1000 * (stop - start), "мс")
