import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

angle_degrees = 30
# radian is radius wrapped around circle
# 360 degress = 2*pi radians

# conversion factor
# the key is that both radians and derees are a measure of movement around a circle.
# degrees to radians: 360/ 2*pi * radians = 180/ (pi  * radians) --degrees per radian or vice versal
# this simple ratio can be wroked either way to convert from one to the other.
angle_radians = np.radians(angle_degrees)

opposite = np.sin(angle_radians)
adjacent = np.cos(angle_radians)
hypotenuse = 1
plt.figure(figsize=(10, 10), dpi=100)
####plt.figure(figsize=(5, 5))
# plt.plot([x1, x2], [y1, y2], 'k-')
plt.plot([0, adjacent], [0, 0], 'r-', label='Adjacent (cos)')
plt.plot([adjacent, adjacent], [0, opposite], 'b-', label='')
plt.plot([0, adjacent], [0, opposite], 'g--', label='Hypotenuse')

# draw the axis
plt.plot([0, 0], [0, 1], 'k--', alpha=0.3)  # Extend y-axis visually
plt.plot([1, 0], [0, 0], 'k--', alpha=0.3)
plt.plot([0, 0], [0, -1], 'k--', alpha=0.3)
plt.plot([-0, 0], [0, 0], 'k--', alpha=0.3)

# Add labels and legend
plt.text(adjacent / 2, -0.05, 'cos(θ)', horizontalalignment='center')
plt.text(adjacent + 0.05, opposite / 2, 'sin(θ)', verticalalignment='center')
plt.text(adjacent / 2 - 0.1, opposite / 2, 'θ', horizontalalignment='center')
plt.legend(loc='upper right')

circle = Circle((0, 0), 1, fill=False, color='blue', linestyle='-', alpha=0.5)
plt.gca().add_patch(circle)
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Unit Circle with Trigonometric Functions')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()
