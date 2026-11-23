
from scipy.io import wavfile

# Чтение аудиофайла
Fs, y = wavfile.read("my_voice.wav")


print("Частота дискретизации:", Fs, "Гц")
print("Количество отсчетов:", len(y))
print("Первые 10 отсчетов:", y[:10])
