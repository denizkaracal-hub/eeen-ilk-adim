# Veri Üretme Scripti - Laboratuvar Simülasyonu
import numpy as np
import pandas as pd

# 1000 tane örneklem noktası (Sample) oluşturalım
t = np.linspace(0, 0.01, 1000) # 0-10 ms arası zaman dilimi

# Temel sinyalimiz: 200 Hz temiz bir sinüs dalgası (Genliği 1V)
temiz_sinyal = 1.0 * np.sin(2 * np.pi * 200 * t)

# Gerçek dünya gürültüsü ekleyelim (Yüksek frekanslı gürültü)
gurultu = 0.3 * np.sin(2 * np.pi * 5000 * t) + 0.1 * np.random.normal(0, 1, 1000)

# Osiloskobun ekranda gördüğü gürültülü sinyal
osiloskop_voltaj = temiz_sinyal + gurultu

# Veriyi bir DataFrame yapıp CSV olarak kaydedelim
df = pd.DataFrame({'Zaman(s)': t, 'Voltaj(V)': osiloskop_voltaj})
df.to_csv('osiloskop_output.csv', index=False)

print("Başarılı! 'osiloskop_output.csv' dosyası 1000 satır veriyle oluşturuldu.")