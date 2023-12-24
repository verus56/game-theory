import numpy as np

M = np.array([[(3, 2), (7, 4), (4, 0)],
              [(4, 2), (8, 4), (5, 0)],
              [(2, 1), (1, 3), (2, 1)],
              [(1, 4), (0, 5), (0, 2)]])




def StrategieDominante(M, i, j):
    ind = -1
    indtemp = -1
    if (i == 1):
        for c in range(len(M[0])):
            val = 0
            for l in range(len(M)):
                if (val < M[l, c, 0]):
                    val = M[l, c, 0]
                    indtemp = l
            if(ind == -1):
                ind = indtemp
            elif (ind != indtemp):
                return -1
        return ind
    if (j == 1):
        for l in range(4):
            val = 0
            for c in range(3):
                if (val < M[l, c, 1]):
                    val = M[l, c, 1]
                    indtemp = c
            if(ind == -1):
                ind = indtemp
            elif (ind != indtemp):
                return -1
        return ind

# Appel de la fonction pour trouver la stratégie dominante du joueur 1 dans la matrice M
resultat_joueur1 = StrategieDominante(M, 1, 0)

# Appel de la fonction pour trouver la stratégie dominante du joueur 2 dans la matrice M
resultat_joueur2 = StrategieDominante(M, 0, 1)

# Affichage des résultats
print("Stratégie dominante du joueur 1:", resultat_joueur1)
print("Stratégie dominante du joueur 2:", resultat_joueur2)
