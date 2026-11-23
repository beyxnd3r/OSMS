
import numpy as np
import matplotlib.pyplot as plt

# Частота исходного сигнала
max_freq = 14 * np.pi / (2 * np.pi)

# Частота дискретизации по теореме Котельникова
min_disk_freq = max_freq * 2

# Исходный сигнал
t = np.linspace(0, 1, 1000)
y = 7 * np.sin(14 * np.pi * t + np.pi / 12)

# Создание массива времени для дискретизации
t_sample = np.arange(0, 1, 1 / min_disk_freq)

# Получение отсчетов сигнала
y_sample = 7 * np.sin(14 * np.pi * t_sample + np.pi / 12)


print("Частота дискретизации:", min_disk_freq, "Гц")
print("Количество отсчетов в секунду:", len(y_sample))
print("Отсчеты:", y_sample)


plt.figure(figsize=(10, 6))

plt.plot(t, y, label="Исходный сигнал", color="blue")
plt.stem(t_sample, y_sample, linefmt="r-",
         markerfmt="ro", basefmt="k-", label="Отсчеты")

plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.title("Дискретизация сигнала при 14 Гц")
plt.grid(True)
plt.legend(loc="upper right")

plt.savefig("results/graphs/task04_digitization.png", dpi=150)
plt.show()
