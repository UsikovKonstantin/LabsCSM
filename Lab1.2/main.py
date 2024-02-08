import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from datetime import datetime
import matplotlib.dates as mdates

# Получаем даты из строк (ось x)
date_strings = ["15.02.2023", "16.02.2023", "17.02.2023", "20.02.2023", "21.02.2023",
                "22.02.2023", "23.02.2023", "24.02.2023", "27.02.2023", "28.02.2023",
                "01.03.2023", "02.03.2023", "03.03.2023", "06.03.2023", "07.03.2023",
                "08.03.2023", "09.03.2023", "10.03.2023", "13.03.2023", "14.03.2023",
                "15.03.2023"]
date_x = [datetime.strptime(date, "%d.%m.%Y") for date in date_strings]
x = mdates.date2num(date_x)

# Данные для оси y
y = [0.6903, 0.6876, 0.6879, 0.6905, 0.6852, 0.6803, 0.6807,
     0.6725, 0.6734, 0.6728, 0.6761, 0.6729, 0.6768, 0.6727,
     0.6582, 0.6586, 0.659, 0.6577, 0.6664, 0.6679, 0.6616]

# Линейный тренд
set_line_by_data = np.polyfit(x, y, 1)
linear_trend = np.poly1d(set_line_by_data)
linear_r2 = r2_score(y, linear_trend(x))

# Полиномиальный тренд
set_polinom_by_data = np.polyfit(x, y, 6)
polinom_trend = np.poly1d(set_polinom_by_data)
polinom_r2 = r2_score(y, polinom_trend(x))

# Логарифмический тренд
set_log_by_data = np.polyfit(np.log(x), y, 1)
log_trend = [set_log_by_data[0] * np.log(x) + set_log_by_data[1] for x in x]
log_r2 = r2_score(y, log_trend)

# Экспоненциальный тренд
set_exp_by_data = np.polyfit(x, np.log(y), 1)
exp_trend = [np.exp(set_exp_by_data[1]) * np.exp(set_exp_by_data[0] * x) for x in x]
exp_r2 = r2_score(y, exp_trend)

# Отображение графиков
plt.figure(figsize=(15, 15))

# Линейный график
plt.subplot(2, 2, 1)
plt.scatter(np.array(date_x), y, label='data')
plt.plot(x, linear_trend(x), linestyle='dashed', color="orange", label='linear trend')
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=10)
plt.title("Линейный \n$R^2=$" + str(linear_r2) + "\n{0}x + {1}".format(*set_line_by_data), fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Полиномиальный график
plt.subplot(2, 2, 2)
plt.scatter(np.array(date_x), y, label='data')
plt.plot(x, polinom_trend(x), linestyle='dashed', color="orange", label='polinomial trend')
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=10)
plt.title("Полиномиальный \n$R^2=$" + str(polinom_r2) + "\n{0}x^6 + {1}x^5 + {2}x^4 + \n{3}x^3 + {4}x^2 + {5}x + \n{6}"
          .format(*set_polinom_by_data), fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Логарифмический график
plt.subplot(2, 2, 3)
plt.scatter(np.array(date_x), y, label='data')
plt.plot(x, log_trend, linestyle='dashed', color="orange", label='log trend')
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=10)
plt.title("Логарифмический \n$R^2=$" + str(log_r2) + "\n{0}ln(x) + {1}".format(*set_log_by_data), fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Экспененциальный график
plt.subplot(2, 2, 4)
plt.scatter(np.array(date_x), y, label='data')
plt.plot(x, exp_trend, linestyle='dashed', color="orange", label='exp trend')
plt.grid(color="gainsboro")
plt.legend(loc='upper right', fontsize=10)
plt.title("Экспоненциальный \n$R^2=$" + str(exp_r2) + "\n{1}e^({0}x)".format(*set_exp_by_data), fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

fig = plt.gcf()
fig.set_size_inches(15, 15)
plt.subplots_adjust(left=0.038, bottom=0.03, right=0.957, top=0.857, wspace=0.186, hspace=0.448)
plt.show()
