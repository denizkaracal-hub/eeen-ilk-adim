import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter

# 1. Dijital Filtre Fonksiyonu (Butterworth Filtresi)
def filtrele(data, cutoff, fs, order=1):
    nyq = 0.5 * fs  # Nyquist Frekansı
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y

# 2. Veriyi Oku
veri = pd.read_csv('osiloskop_output.csv')
zaman = veri['Zaman(s)']
gurultulu_voltaj = veri['Voltaj(V)']

# 3. Filtre Parametreleri
# 1000 örnek 0.01 saniyede alındığı için Örnekleme Frekansı (fs) = 100.000 Hz
fs = 100000.0       
cutoff = 1600.0  # Bizim meşhur 1.6 kHz kesim frekansımız

# Filtreyi çalıştır
temiz_voltaj = filtrele(gurultulu_voltaj, cutoff, fs, order=1)

# 4. İki Sinyali Alt Alta Çizdirme
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Üst Grafik: Ham Veri
ax1.plot(zaman * 1000, gurultulu_voltaj, color='red', alpha=0.6)
ax1.set_title('Filtre Öncesi: Ham Osiloskop Sinyali (Gürültülü 200Hz + 5kHz)')
ax1.set_ylabel('Voltaj (V)')
ax1.grid(True)

# Alt Grafik: Filtrelenmiş Veri
ax2.plot(zaman * 1000, temiz_voltaj, color='green', linewidth=2)
ax2.set_title('Filtre Sonrası: Dijital LPF Sinyali (Yüksek Frekans Tıraşlandı)')
ax2.set_xlabel('Zaman (ms)')
ax2.set_ylabel('Voltaj (V)')
ax2.grid(True)

plt.tight_layout()
plt.show()