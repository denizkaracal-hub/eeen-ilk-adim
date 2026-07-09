# EEEN Filtre Analiz Scripti - 2026
import math

print("--- Alçak Geçiren Filtre Analiz Aracı ---")

# Giriş Voltajı (V_in = 1V AC)
v_in = 1.0

# Kesim frekansı formülü: fc = 1 / (2 * pi * R * C)
# Bizim devremiz: R = 1000 Ohm, C = 100nF (0.0000001 Farad)
R = 1000
C = 100e-9 
f_c = 1 / (2 * math.pi * R * C)

print(f"Teorik Kesim Frekansı (fc): {f_c:.2f} Hz (~1.6 kHz)")

# Ölçülen bazı frekans değerlerini test edelim
test_frekanslari = [100, 500, 1590, 5000, 10000]

print("\n--- Farklı Frekanslardaki Çıkış Voltajları (V_out) ---")
for f in test_frekanslari:
    # Frekansa göre kazanç (Gain) hesaplama formülü
    kazanc = 1 / math.sqrt(1 + (f / f_c)**2)
    v_out = v_in * kazanc
    
    # dB cinsinden kazanç
    db = 20 * math.log10(kazanc)
    
    print(f"Frekans: {f:5d} Hz | V_out: {v_out:.3f} V | Kazanç: {db:.2f} dB")
    if f == 1590:
        print("  -> Tam kesim frekansında voltaj 0.707V'a, kazanç -3dB'e düştü!")