
import numpy as np
import matplotlib.pyplot as plt

from dft import calculate_dft

# Частота исходного сигнала
max_freq = 14 * np.pi / (2 * np.pi)

# Частота дискретизации
min_disk_freq = max_freq * 2

# Исходный сигнал
t_sample = np.arange(0, 1, 1 / min_disk_freq)

y_sample = 7 * np.sin(
    14 * np.pi * t_sample + np.pi / 12
)

# Прямое дискретное преобразование Фурье
frequencies, amplitude = calculate_dft(
    y_sample, min_disk_freq
)


print("Частота дискретизации:", min_disk_freq, "Гц")
print("Количество отсчетов:", len(y_sample))

print("Частоты спектра:", frequencies)
print("Амплитуды спектра:", amplitude)


print("Максимальная частота спектра:",
      np.max(np.abs(frequencies)), "Гц")

# Объем памяти
print("Объем памяти:", y_sample.nbytes, "байт")

# Построение амплитудного спектра
plt.figure(figsize=(10, 5))

plt.stem(frequencies, amplitude)

plt.xlabel("Частота (Гц)")
plt.ylabel("Модуль спектра")
plt.title("Амплитудный спектр сигнала при 14 Гц")
plt.grid(True)

plt.savefig(
    "results/graphs/task05_dft.png",
    dpi=150
)

plt.show()
