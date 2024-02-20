import matplotlib.pyplot as plt
import numpy as np

# Generate an array of angles from 0 to 2*pi (360 degrees)
angles = np.linspace(0, 2 * np.pi, 400)

# Compute sine and cosine of these angles
sine_wave = np.sin(angles)
cosine_wave = np.cos(angles)

# Plotting sine and cosine waves
plt.figure(figsize=(10, 5))
plt.plot(angles, sine_wave, label='Sine Wave')
plt.plot(angles, cosine_wave, label='Cosine Wave', linestyle='--')

# Adding labels and legend
plt.xlabel('Angle (radians)')
plt.ylabel('Function value')
plt.title('Sine and Cosine Waves')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()
