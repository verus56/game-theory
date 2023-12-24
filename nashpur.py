import numpy as np

def find_pure_nash_equilibria(matrix):
    num_rows, num_cols = matrix.shape[:2]  # Use slicing to only get the first two elements of the shape tuple

    pure_nash_equilibria = []

    for i in range(num_rows):
        for j in range(num_cols):
            # Vérification si la stratégie (i, j) est un équilibre de Nash pur
            is_nash = all(matrix[i, k][1] <= matrix[i, j][1] for k in range(num_cols)) and \
                      all(matrix[k, j][0] <= matrix[i, j][0] for k in range(num_rows))
            
            if is_nash:
                pure_nash_equilibria.append((i, j))

    return pure_nash_equilibria

# Exemple d'utilisation
matrix_example = np.array([[(4, 3), (5, 1), (6, 2)],
                            [(2, 1), (8, 4), (3, 6)],
                            [(3, 0), (9, 6), (2, 8)]])
equilibria = find_pure_nash_equilibria(matrix_example)

if not equilibria:
    print("Aucun équilibre de Nash pur trouvé.")
else:
    print("Équilibres de Nash purs trouvés aux positions :", equilibria)

#*****************************************************************************************#

# Nouvelle matrice d'exemple
#new_matrix_example = np.array([[(1, 2), (3, 4), (5, 6)],
                               #[(7, 8), (9, 10), (11, 12)],
                               #[(13, 14), (15, 16), (17, 18)]])

# Appel de la fonction avec la nouvelle matrice
#new_equilibria = find_pure_nash_equilibria(new_matrix_example)

# Affichage des résultats
#if not new_equilibria:
    #print("Aucun équilibre de Nash pur trouvé.")
#else:
    #print("Équilibres de Nash purs trouvés aux positions :", new_equilibria)


