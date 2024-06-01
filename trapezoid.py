import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Implementasi metode integrasi trapezoid
def trapezoid_integration(f, a, b, N):
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b - a) / N
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Hasil perhitungan dan evaluasi
for N in N_values:
    start_time = time.time()
    pi_estimate = trapezoid_integration(f, 0, 1, N)
    end_time = time.time()
    rms_error = np.sqrt((pi_estimate - pi_reference)**2)
    execution_time = end_time - start_time

    print(f"N = {N}")
    print(f"Estimasi pi: {pi_estimate}")
    print(f"Galat RMS: {rms_error}")
    print(f"Waktu eksekusi: {execution_time} detik\n")
