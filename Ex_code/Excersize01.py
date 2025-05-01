import numpy as np
import matplotlib.pyplot as plt

# Parameters
V_m = 10       # Peak voltage (Volts)
f = 50         # Frequency (Hz)
omega = 2 * np.pi * f  # Angular frequency
L = 0.1        # Inductance (Henries)
R = 10         # Resistance (Ohms)
t = np.linspace(0, 0.1, 1000)  # Time vector for 100 ms

# Voltage source
v = V_m * np.sin(omega * t)

# Case 1: Pure Inductor (R=0)
# i_L = integral(v/L) dt = -(Vm/ωL) * cos(ωt) + constant (set so i(0) = 0)
i_L = -(V_m / omega / L) * np.cos(omega * t) + (V_m / omega / L)

# Case 2: RL Circuit (R > 0)
phi = np.arctan(omega * L / R)
I_m = V_m / np.sqrt(R**2 + (omega * L)**2)
i_RL = I_m * np.sin(omega * t - phi) * (1 - np.exp(-R * t / L))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t * 1000, i_L, label="Pure Inductor (R=0)", linestyle='--')
plt.plot(t * 1000, i_RL, label="RL Circuit (R>0)", linewidth=2)
plt.xlabel("Time (ms)")
plt.ylabel("Current (A)")
plt.title("Current Response in Inductive and RL Circuits")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
