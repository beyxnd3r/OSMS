
import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0, 1, 1/1000)

# Исходный сигнал 
y_signal = 7 * np.sin(14 * np.pi * t + np.pi / 12)


print("Количество отсчетов:", len(y_signal))
print("Минимальная амплитуда:", np.min(y_signal))
print("Максимальная амплитуда:", np.max(y_signal))


plt.figure(figsize=(10, 5))

plt.plot(t, y_signal)

plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.title("Исходный сигнал")
plt.grid(True)


plt.savefig("results/graphs/task01_signal.png", dpi=150)

plt.show()
