import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV Dosyasını İçeri Aktar
veri = pd.read_csv('osiloskop_output.csv')

# Verileri değişkenlere ata
zaman = veri['Zaman(s)']
voltaj = veri['Voltaj(V)']

# 2. Matplotlib ile Grafik Çizdirme
plt.figure(figsize=(10, 5))
plt.plot(zaman * 1000, voltaj, label='Gürültülü Osiloskop Verisi', color='red', alpha=0.7)

plt.title('Laboratuvardan Alınan Ham Osiloskop Sinyali (2026)')
plt.xlabel('Zaman (Milisaniye - ms)')
plt.ylabel('Voltaj (V)')
plt.grid(True)
plt.legend()

# Grafiği ekranda göster
plt.show()