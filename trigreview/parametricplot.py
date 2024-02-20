import numpy as np
import matplotlib.pyplot as plt

# Generate a range of angles from 0 to 2*pi radians
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate x and y coordinates of points on the circle
x = np.cos(theta)
y = np.sin(theta)

# Plot the circle
plt.figure(figsize=(5, 5))
plt.plot(x, y)
plt.title('Unit Circle')
plt.xlabel('Cosine (x)')
plt.ylabel('Sine (y)')
plt.grid(True)
plt.axis('equal')  # Ensure the aspect ratio is equal to make the circle look round
plt.show()
