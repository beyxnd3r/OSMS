import numpy as np
import math


def calculate_dft(signal, sampling_frequency):
    # Количество отсчетов
    N = len(signal)

    # Массивы для действительной и мнимой частей
    real = np.zeros(N)
    imaginary = np.zeros(N)

    # Прямое дискретное преобразование Фурье
    for k in range(N):
        for n in range(N):
            angle = 2 * math.pi * k * n / N

            real[k] += signal[n] * math.cos(angle)
            imaginary[k] -= signal[n] * math.sin(angle)

    # Вычисление амплитуд спектра
    amplitude = np.zeros(N)

    for k in range(N):
        amplitude[k] = math.sqrt(real[k] ** 2 + imaginary[k] ** 2)

    # Вычисление частот
    frequencies = np.zeros(N)

    for k in range(N):
        if k <= N // 2:
            frequencies[k] = k * sampling_frequency / N
        else:
            frequencies[k] = (k - N) * sampling_frequency / N

    return frequencies, amplitude