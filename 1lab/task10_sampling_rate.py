
from scipy.io import wavfile

# Чтение аудиофайла
Fs, y = wavfile.read("my_voice.wav")

# Количество отсчетов
N = len(y)

# Длительность записи
duration = N / Fs

# Вычисление частоты дискретизации
calculated_fs = N / duration


print("Количество отсчетов:", N)
print("Длительность записи:", duration, "с")
print("Частота дискретизации по WAV:", Fs, "Гц")
print("Вычисленная частота дискретизации:", calculated_fs, "Гц")


if abs(calculated_fs - Fs) < 0.001:
    print("Результаты совпадают.")
else:
    print("Результаты не совпадают.")
