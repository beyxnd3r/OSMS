import numpy as np
import matplotlib.pyplot as plt
from math import log10, ceil

f = 1800
f_ghz = 1.8
bw_ul = 10e6
bw_dl = 20e6

noise_ul = -174 + 10 * log10(bw_ul)
noise_dl = -174 + 10 * log10(bw_dl)

sensitivity_bs = 2.4 + noise_ul + 4
sensitivity_ue = 6 + noise_dl + 2

feeder = 2 + 0.4 + 0.5
max_path_loss_ul = 24 - feeder + 21 + 3 - 1 - 15 - sensitivity_bs
max_path_loss_dl = 46 - feeder + 21 + 3 - 1 - 15 - sensitivity_ue

print("Thermal noise UL:", round(noise_ul, 2), "dBm")
print("Thermal noise DL:", round(noise_dl, 2), "dBm")
print("RxSens BS:", round(sensitivity_bs, 2), "dBm")
print("RxSens UE:", round(sensitivity_ue, 2), "dBm")
print("MAPL UL:", round(max_path_loss_ul, 2), "dB")
print("MAPL DL:", round(max_path_loss_dl, 2), "dB")

def umi(d):
    return 26 * np.log10(f_ghz) + 22.7 + 36.7 * np.log10(d)

def cost231(d):
    h_bs = 30
    h_ms = 1.5
    l_clutter = 0

    a = 3.2 * (np.log10(11.75 * h_ms))**2 - 4.97

    s = np.where(d >= 1, 44.9 - 6.55 * np.log10(h_bs), (47.88 + 13.9 * np.log10(f) - 13.9 * np.log10(h_bs)) / log10(50))

    return 46.3 + 33.9 * np.log10(f) - 13.82 * np.log10(h_bs) - a + s * np.log10(d) + l_clutter

def walfish(d):
    h_bs = 30
    h_ms = 1.5
    h_building = 20
    w = 20
    b = 50
    phi = 45
    delta_h = h_building - h_ms
    l0 = 32.44 + 20 * np.log10(f) + 20 * np.log10(d)
    lori = 2.5 + 0.075 * phi
    l2 = -16.9 - 10 * np.log10(w) + 10 * np.log10(f) + 20 * np.log10(delta_h) + lori
    l11 = -18 * np.log10(1 + h_bs - h_building)
    ka = 54
    kd = 18
    kf = -4 + 0.7 * (f / 925 - 1)
    l1 = l11 + ka + kd * np.log10(d) + kf * np.log10(f) - 9 * np.log10(b)
    return np.where(l1 + l2 > 0, l0 + l1 + l2, l0)

distance_km = np.linspace(0.01, 10, 1000)
distance_m = distance_km * 1000

plt.plot(distance_m, umi(distance_m), color="#2563eb", linewidth=2, label="UMiNLOS")
plt.plot(distance_m, cost231(distance_km), color="#d97706", linewidth=2, label="COST231-Hata")
plt.plot(distance_m, walfish(distance_km), color="#059669", linewidth=2, label="Walfish-Ikegami")
plt.axhline(max_path_loss_ul, color="#7c3aed", linestyle="--", linewidth=1.5, label="MAPL UL")
plt.axhline(max_path_loss_dl, color="#dc2626", linestyle=":", linewidth=1.8, label="MAPL DL")
plt.xlabel("Расстояние, м")
plt.ylabel("Потери сигнала, дБ")
plt.grid(True, linestyle="--", alpha=0.45)
plt.legend()
plt.tight_layout()
plt.show()

d = np.linspace(0.03, 10, 10000)
pl = cost231(d)
radius_ul = d[np.argmin(abs(pl - max_path_loss_ul))]
radius_dl = d[np.argmin(abs(pl - max_path_loss_dl))]
r = min(radius_ul, radius_dl)
coverage_area = 1.95 * r**2
stations = ceil(100 / coverage_area)

print("------------------------------------------------------")
print("Макросота COST231-Hata")
print("R UL:", round(radius_ul, 3), "km")
print("R DL:", round(radius_dl, 3), "km")
print("Радиус соты:", round(r, 3), "km")
print("Площадь БС:", round(coverage_area, 3), "km^2")
print("Число БС на 100 km^2:", stations)

radius_ul_umi = 10 ** ((max_path_loss_ul - 26 * log10(f_ghz) - 22.7) / 36.7)
radius_dl_umi = 10 ** ((max_path_loss_dl - 26 * log10(f_ghz) - 22.7) / 36.7)
radius_umi = min(radius_ul_umi, radius_dl_umi)
coverage_area_umi = 1.95 * (radius_umi / 1000)**2
stations_umi = ceil(4 / coverage_area_umi)

print("------------------------------------------------------")
print("Микро-/фемтосота UMiNLOS")
print("R UL:", round(radius_ul_umi, 1), "m")
print("R DL:", round(radius_dl_umi, 1), "m")
print("Радиус соты:", round(radius_umi, 1), "m")
print("Площадь БС:", round(coverage_area_umi, 4), "km^2")
print("Число БС на 4 km^2:", stations_umi)
