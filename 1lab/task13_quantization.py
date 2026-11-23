
import numpy as np
import matplotlib.pyplot as plt
import math
import os


# Исходный сигнал
Fs = 1000
t = np.arange(0, 1, 1 / Fs)

y = 7 * np.sin(14 * np.pi * t + np.pi / 12)


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

        amplitude[k] = math.sqrt(real ** 2 + imag ** 2) / N

        if k != 0 and not (N % 2 == 0 and k == N // 2):
            amplitude[k] *= 2

        frequencies[k] = k * Fs / N

    return frequencies, amplitude


# Квантование сигнала с учетом разрядности АЦП
def quantize_signal(signal, bits):
    levels = 2 ** bits

    signal_min = np.min(signal)
    signal_max = np.max(signal)

    # Преобразование амплитуд в диапазон цифровых кодов
    codes = (
        (signal - signal_min) /
        (signal_max - signal_min) *
        (levels - 1)
    )

    # Округление до ближайшего цифрового кода
    codes = np.round(codes)

    # Ограничение кодов диапазоном АЦП
    codes = np.clip(codes, 0, levels - 1)

    # Восстановление амплитудного диапазона
    restored = (
        codes / (levels - 1) *
        (signal_max - signal_min) + signal_min
    )

    return restored


# Спектр исходного сигнала
frequencies, amplitude_original = calculate_dft(y, Fs)

# Разрядности АЦП
bit_depths = [3, 4, 5, 6]

os.makedirs("results/graphs", exist_ok=True)


fig, axes = plt.subplots(2, 2, figsize=(13, 9))
axes = axes.flatten()

print("Результаты квантования:\n")

errors = []

for i, bits in enumerate(bit_depths):

    # Квантование сигнала
    y_quantized = quantize_signal(y, bits)

    # Количество уровней
    levels = 2 ** bits

    # Средняя абсолютная ошибка квантования
    error = np.mean(np.abs(y - y_quantized))
    errors.append(error)

    # ДПФ квантованного сигнала
    frequencies_q, amplitude_q = calculate_dft(y_quantized, Fs)

    print("Разрядность АЦП:", bits, "бит")
    print("Количество уровней:", levels)
    print("Диапазон цифровых кодов: 0 -", levels - 1)
    print("Средняя ошибка квантования:", error)
    print()

    # Сравнение спектров
    axes[i].plot(
        frequencies,
        amplitude_original,
        label="Исходный сигнал"
    )

    axes[i].plot(
        frequencies_q,
        amplitude_q,
        label="Квантованный сигнал"
    )

    axes[i].set_title(str(bits) + " бит")
    axes[i].set_xlabel("Частота (Гц)")
    axes[i].set_ylabel("Амплитуда")
    axes[i].set_xlim(0, 50)
    axes[i].grid(True)
    axes[i].legend()


plt.suptitle("Влияние разрядности АЦП на спектр сигнала")
plt.tight_layout()

plt.savefig(
    "results/graphs/task13_quantization.png",
    dpi=150
)

plt.show()



plt.figure(figsize=(12, 6))

plt.plot(
    t[:100],
    y[:100],
    label="Исходный сигнал",
    linewidth=2
)

for bits in bit_depths:

    y_quantized = quantize_signal(y, bits)

    plt.plot(
        t[:100],
        y_quantized[:100],
        marker=".",
        label=str(bits) + " бит"
    )

plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.title("Влияние разрядности АЦП на форму сигнала")
plt.grid(True)
plt.legend()

plt.savefig(
    "results/graphs/task13_quantization_signal.png",
    dpi=150
)

plt.show()



print("Сравнение средней ошибки квантования:")

for i in range(len(bit_depths)):
    print(
        bit_depths[i],
        "бит:",
        round(errors[i], 6)
    )
