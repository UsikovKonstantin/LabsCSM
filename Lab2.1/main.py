from math import pi
from scipy import fft
from numpy import arange, cos
import numpy as np
import matplotlib.pyplot as plt

A = 3
T = 200
dT = 1
fi = pi / 6
n = 1.45
k = arange(0, 1024)

s = (2 * pi * (0.3 * k)**n * dT) / T
# Функция сигнала
x1 = A * cos(s + fi) + 2
# Прямое преобразование Фурье
y = fft.fft(x1)
abs_y = np.real(y)
# Обратное преобразование Фурье
F = fft.ifft(y)
# Вектор частот
f = k / 1024


# Отображение графиков
plt.figure(figsize=(15, 15))

# Функция сигнала
plt.subplot(3, 1, 1)
plt.plot(k, x1, label='data', marker=None, linewidth=1)
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=10)
plt.title("Функция сигнала", fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Прямое преобразование Фурье
plt.subplot(3, 1, 2)
plt.plot(k, abs_y, label='data', marker=None, linewidth=1)
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=10)
plt.title("Прямое преобразование Фурье", fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Обратное преобразование Фурье
plt.subplot(3, 1, 3)
plt.plot(k, F, label='data', marker=None, linewidth=1)
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=10)
plt.title("Обратное преобразование Фурье", fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

fig = plt.gcf()
fig.set_size_inches(15, 15)
plt.subplots_adjust(left=0.026, bottom=0.029, right=0.99, top=0.971, wspace=0, hspace=0.35)
plt.show()
