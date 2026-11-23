
import numpy as np
import matplotlib.pyplot as plt

# Исходные параметры
max_freq = 14 * np.pi / (2 * np.pi)

# Исходная частота дискретизации
min_disk_freq = max_freq * 2

# Увеличение частоты дискретизации в 4 раза
new_freq = min_disk_freq * 4

# Исходный сигнал
t = np.linspace(0, 1, 1000)
y = 7 * np.sin(14 * np.pi * t + np.pi / 12)

# Новые временные точки дискретизации
t_sample_x4 = np.arange(0, 1, 1 / new_freq)

# Получение новых отсчетов
y_sample_x4 = 7 * np.sin(
    14 * np.pi * t_sample_x4 + np.pi / 12
)


print("Исходная частота дискретизации:", min_disk_freq, "Гц")
print("Новая частота дискретизации:", new_freq, "Гц")
print("Новое количество отсчетов:", len(y_sample_x4))
print("Отсчеты:", y_sample_x4)


plt.figure(figsize=(10, 5))

plt.plot(t, y, label="Исходный сигнал", color="blue")

plt.stem(
    t_sample_x4,
    y_sample_x4,
    linefmt="r-",
    markerfmt="ro",
    basefmt="k-",
    label="Отсчеты (56 Гц)"
)

plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.title("Дискретизация сигнала при 56 Гц")
plt.grid(True)
plt.legend(loc="upper right")

plt.savefig(
    "results/graphs/task07_sampling_x4.png",
    dpi=150
)

plt.show()
