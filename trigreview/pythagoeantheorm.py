import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Parameters for the triangle sides
a = 3
b = 4
c = (a**2 + b**2)**0.5  # Hypotenuse

# Create figure and axis
fig, ax = plt.subplots()

# Large Square
large_square = patches.Rectangle((0, 0), a+b, a+b, edgecolor='black', facecolor='none')
ax.add_patch(large_square)

# Smaller square (c^2)
small_square = patches.Rectangle((b, 0), a, a, edgecolor='black', facecolor='none')
ax.add_patch(small_square)

# Four triangles (color-coded)
triangle1 = patches.Polygon([[0, 0], [b, 0], [b, a]], closed=True, edgecolor='red', facecolor='lightgrey', label='Triangle 1')
triangle2 = patches.Polygon([[b, 0], [b+a, 0], [b, a]], closed=True, edgecolor='blue', facecolor='lightgrey', label='Triangle 2')
triangle3 = patches.Polygon([[b, a], [b, a+b], [b+a, a]], closed=True, edgecolor='green', facecolor='lightgrey', label='Triangle 3')
triangle4 = patches.Polygon([[b, a+b], [0, a+b], [b, a]], closed=True, edgecolor='orange', facecolor='lightgrey', label='Triangle 4')

ax.add_patch(triangle1)
ax.add_patch(triangle2)
ax.add_patch(triangle3)
ax.add_patch(triangle4)

# Annotations
ax.text(b/2, -0.5, '$b$', ha='center', fontsize=12)
ax.text(b + a/2, -0.5, '$a$', ha='center', fontsize=12)
ax.text(b + a + 0.5, a/2, '$a$', va='center', fontsize=12)
ax.text(-0.5, a/2, '$b$', va='center', fontsize=12)
ax.text(b/2, a/2, '$c^2$', ha='center', va='center', fontsize=12, color='red')

# Set aspect of the plot to be equal
ax.set_aspect('equal', 'box')

# Remove axes
ax.axis('off')

plt.title('Pythagorean Theorem Proof')
plt.show()
