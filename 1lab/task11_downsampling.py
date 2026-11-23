
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import subprocess

# Чтение исходного аудиофайла
Fs, y = wavfile.read("my_voice.wav")


print("Исходная частота дискретизации:", Fs, "Гц")
print("Исходное количество отсчетов:", len(y))

# Понижение частоты дискретизации в 10 раз
y1 = y[::10]

# Новая частота дискретизации
Fs1 = Fs / 10


print("Пониженная частота дискретизации:", Fs1, "Гц")
print("Количество отсчетов после прореживания:", len(y1))


wavfile.write(
    "results/audio/my_voice_lowered.wav",
    int(Fs1),
    y1
)


t = np.arange(len(y1)) / Fs1


plt.figure(figsize=(12, 5))

plt.plot(t, y1)

plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.title("Голосовой сигнал")
plt.grid(True)

plt.savefig(
    "results/graphs/task11_downsampling.png",
    dpi=150
)

plt.show()


print("Воспроизведение измененного аудиосигнала...")

subprocess.run([
    "powershell.exe",
    "-Command",
    "(New-Object Media.SoundPlayer 'results/audio/my_voice_lowered.wav').PlaySync()"
])

print("Воспроизведение завершено.")
