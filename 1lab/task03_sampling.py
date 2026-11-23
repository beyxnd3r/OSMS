
import numpy as np

# Максимальная частота сигнала
max_freq = 14 * np.pi / (2 * np.pi)

# Минимальная частота дискретизации
min_disk_freq = max_freq * 2

print("Максимальная частота сигнала:", max_freq, "Гц")
print("Минимальная частота дискретизации:", min_disk_freq, "Гц")