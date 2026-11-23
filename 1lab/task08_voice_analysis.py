# рассчеты для задания 8
# максимальная частота сигнала = 6669 Гц
# частота дискретизации = 6669 * 2 = 13338 Гц


import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Чтение голосовой записи
fs, y_voice = wavfile.read("my_voice.wav")

# Определение характеристик записи
duration = len(y_voice) / fs

print("Частота дискретизации:", fs, "Гц")
print("Количество отсчетов:", len(y_voice))
print("Длительность записи:", round(duration, 2), "с")
print("Минимальное значение:", np.min(y_voice))
print("Максимальное значение:", np.max(y_voice))


max_voice_freq = 6669

# Расчет необходимой частоты дискретизации
required_fs = max_voice_freq * 2


selected_fs = 16000

print("\nМаксимальная частота голоса:", max_voice_freq, "Гц")
print("Минимальная частота дискретизации:", required_fs, "Гц")
print("Выбранная частота дискретизации:", selected_fs, "Гц")


t_voice = np.arange(len(y_voice)) / fs


plt.figure(figsize=(12, 5))

plt.plot(t_voice, y_voice)

plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.title("Временное представление голосового сигнала")
plt.grid(True)

plt.savefig(
    "results/graphs/task08_voice_analysis.png",
    dpi=150
)

plt.show()
