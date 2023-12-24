import numpy as np

def pareto_dominance(points):
    num_points, num_criteria = points.shape[:2]
    is_dominated = np.zeros(num_points, dtype=bool)

    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                if np.all(points[i] <= points[j]):
                    is_dominated[i] = True
                    break

    pareto_dominant_points = points[~is_dominated]
    return pareto_dominant_points

# Exemple d'utilisation
#matrix_example = np.array([[(4, 3), (5, 1), (6, 2)],
                           #[(2, 1), (8, 4), (3, 6)],
                           #[(3, 0), (9, 6), (2, 8)]])

matrix_example = np.array([[(1, 2), (3, 4), (5, 6)],
                               [(7, 8), (9, 10), (11, 12)],
                               [(13, 14), (15, 16), (17, 18)]])

matrix_flattened = matrix_example.reshape(-1, matrix_example.shape[-1])
pareto_points = pareto_dominance(matrix_flattened)

print("Points de Pareto dominants :")
print(pareto_points)

