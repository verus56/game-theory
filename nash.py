import numpy as np
from scipy.optimize import linprog

def find_nash_equilibria(matrix):
    row_player_payoffs = -matrix  # Conversion en forme standard pour maximiser
    num_rows, num_cols = matrix.shape

    # Contraintes pour le joueur de ligne (somme des stratégies égale à 1)
    row_constraints = np.ones((1, num_rows))

    # Contraintes pour le joueur de colonne (somme des stratégies égale à 1)
    col_constraints = np.ones((1, num_cols))

    # Fonction objectif du joueur de ligne (minimiser)
    c_row = np.zeros(num_rows)

    # Fonction objectif du joueur de colonne (maximiser)
    c_col = np.ones(num_cols)

    # Résolution du problème d'optimisation linéaire pour le joueur de ligne
    result_row = linprog(c_row, A_eq=row_constraints, b_eq=[1])

    # Résolution du problème d'optimisation linéaire pour le joueur de colonne
    result_col = linprog(c_col, A_eq=col_constraints, b_eq=[1])

    # Les solutions optimales correspondent aux stratégies mixtes optimales pour les joueurs
    row_strategy = result_row.x
    col_strategy = result_col.x

    # Calcul des payoffs des joueurs avec les stratégies mixtes optimales
    row_payoff = row_strategy @ row_player_payoffs @ col_strategy

    # Vérification si les stratégies mixtes sont des équilibres de Nash
    is_nash = np.isclose(row_payoff, 0)

    # Affichage des résultats
    print("Stratégies mixtes optimales pour le joueur de ligne:", row_strategy)
    print("Stratégies mixtes optimales pour le joueur de colonne:", col_strategy)
    print("Payoff du joueur de ligne:", row_payoff)
    print("Est-ce un équilibre de Nash?", is_nash)

# Exemple d'utilisation
matrix_example = np.array([[3, 1], [2, 4]])
find_nash_equilibria(matrix_example)
