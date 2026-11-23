
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os


# Прямое дискретное преобразование Фурье
def calculate_dft(signal, Fs):
    N = len(signal)

    frequencies = np.zeros(N // 2 + 1)
    amplitude = np.zeros(N // 2 + 1)

    n = np.arange(N)

    for k in range(N // 2 + 1):
        angle = 2 * np.pi * k * n / N

        real = np.sum(signal * np.cos(angle))
        imag = -np.sum(signal * np.sin(angle))

        amplitude[k] = np.sqrt(real ** 2 + imag ** 2) / N

        if k != 0 and not (N % 2 == 0 and k == N // 2):
            amplitude[k] *= 2

        frequencies[k] = k * Fs / N

    return frequencies, amplitude


# Чтение исходной записи
Fs, y = wavfile.read("my_voice.wav")

# Чтение прореженной записи
Fs1, y1 = wavfile.read("results/audio/my_voice_lowered.wav")

# Преобразование стерео в моно, если необходимо
if y.ndim == 2:
    y = np.mean(y, axis=1)

if y1.ndim == 2:
    y1 = np.mean(y1, axis=1)


y = y.astype(float)
y1 = y1.astype(float)

# Выбираем одинаковый временной участок
N = 4096
N1 = 410

y_part = y[:N]
y1_part = y1[:N1]

# Вычисление ДПФ
frequencies, amplitude = calculate_dft(y_part, Fs)
frequencies1, amplitude1 = calculate_dft(y1_part, Fs1)


print("Исходный сигнал:")
print("Частота дискретизации:", Fs, "Гц")
print("Количество отсчетов:", len(y_part))
print("Максимальная частота спектра:", frequencies[-1], "Гц")

print("\nПрореженный сигнал:")
print("Частота дискретизации:", Fs1, "Гц")
print("Количество отсчетов:", len(y1_part))
print("Максимальная частота спектра:", frequencies1[-1], "Гц")


os.makedirs("results/graphs", exist_ok=True)

# Построение двух отдельных графиков
fig, axes = plt.subplots(2, 1, figsize=(12, 9))

# Спектр исходного сигнала
axes[0].plot(frequencies, amplitude)
axes[0].set_title("Спектр исходного голосового сигнала")
axes[0].set_xlabel("Частота (Гц)")
axes[0].set_ylabel("Амплитуда")
axes[0].set_xlim(0, Fs / 2)
axes[0].grid(True)

# Спектр прореженного сигнала
axes[1].plot(frequencies1, amplitude1, color="orange")
axes[1].set_title("Спектр прореженного голосового сигнала")
axes[1].set_xlabel("Частота (Гц)")
axes[1].set_ylabel("Амплитуда")
axes[1].set_xlim(0, Fs1 / 2)
axes[1].grid(True)

plt.tight_layout()

plt.savefig(
    "results/graphs/task12_voice_dft.png",
    dpi=150
)

plt.show()
