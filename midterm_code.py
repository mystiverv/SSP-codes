import numpy as np
import matplotlib.pyplot as plt

# lattice parameters and reciprocal lattice vectors 
a = .132  # Lattice parameter
b1 = (2 * np.pi / (3 * a)) * np.array([np.sqrt(3), -1])
b2 = (2 * np.pi / (3 * a)) * np.array([-np.sqrt(3), -1])

#max number of lattice points ,edit if you want
num_points_x = 5
num_points_y = 5

#empty list for storing lattice points
lattice_points = []

# Generate lattice points
for i in range(num_points_x):
    for j in range(num_points_y):
        lattice_point = i * b1 + j * b2
        lattice_points.append(lattice_point)

lattice_points = np.array(lattice_points)

#plots lattice points
plt.scatter(lattice_points[:, 0], lattice_points[:, 1])
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('kx')
plt.ylabel('ky')
plt.title('2D Lattice')
plt.grid()
plt.show()

