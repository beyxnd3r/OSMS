
import numpy as np
import matplotlib.pyplot as plt

# Частота исходного сигнала
max_freq = 14 * np.pi / (2 * np.pi)

# Частота дискретизации
min_disk_freq = max_freq * 2

# Исходный сигнал
t = np.linspace(0, 1, 1000)
y = 7 * np.sin(14 * np.pi * t + np.pi / 12)

# Временные точки дискретизации
t_sample = np.arange(0, 1, 1 / min_disk_freq)

# Получение отсчетов
y_sample = 7 * np.sin(
    14 * np.pi * t_sample + np.pi / 12
)


plt.figure(figsize=(10, 5))


plt.plot(
    t, y,
    label="Исходный сигнал",
    color="blue"
)


plt.plot(
    t_sample, y_sample,
    "o-",
    label="Восстановленный сигнал",
    color="orange"
)

plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.title("Сравнение исходного и восстановленного сигналов")
plt.grid(True)
plt.legend(loc="upper right")

plt.savefig(
    "results/graphs/task06_reconstruction.png",
    dpi=150
)

plt.show()


print("Частота дискретизации:", min_disk_freq, "Гц")
print("Количество отсчетов:", len(y_sample))
