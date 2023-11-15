import numpy as np
import matplotlib.pyplot as plt

def fcc_lattice_points(n):
    points = []
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            for k in range(-n, n+1):
                # lattice vectors for fcc
                points.append([i + 0.5*j + 0.5*k, 0.5*i + j + 0.5*k, 0.5*i + 0.5*j + k])
    return np.array(points)

# computes vdw sum
def vdw_force(r):
    #equation 10 from kittel
    return 4*(1.0 / r**12 - 1.0 / r**6)

# calculates sum for given atoms
def compute_vdw_sum(num_atoms):
    lattice = fcc_lattice_points(int(np.cbrt(num_atoms)))
    reference = np.array([0, 0, 0])
    total_sum = 0
    
    for point in lattice:
        distance = np.linalg.norm(reference - point)
        if distance != 0:  # excludes reference atom
            total_sum += vdw_force(distance)
    
    return total_sum


def plot_vdw_sums(atom_counts):
    sums = [compute_vdw_sum(count) for count in atom_counts]

  
    plt.figure(figsize=(10, 6))
    plt.plot(atom_counts, sums, '-o', color='blue')
    plt.title('Van der Waals Sums vs. Number of Atoms')
    plt.xlabel('Number of Atoms')
    plt.ylabel('VDW Sum')
    plt.grid(True)
    plt.show()

#atoms count starting with beginning range of values then going to 100,000 ib increments of 10,000
atom_counts = [1, 12, 50, 100, 250, 500, 1000, 5000, 10000] + [x for x in range(20000, 100000, 10000)]
plot_vdw_sums(atom_counts)
