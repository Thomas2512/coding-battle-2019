import math
import numpy as np
from itertools import permutations


# On récupère tous les inputs...
Q = int(input())
N = int(input())

jaune = []
bleu = []

for i in range(N):
    a = input()
    if int(a[0]) == 1:
        jaune.append(int(str(a)[2:]))
    else:
        bleu.append(int(str(a)[2:]))
# Les inputs ont tous été récupérés

# On construit la matrice des énergies de toutes les paires (jaune, bleu) possibles
matrix = np.zeros((len(jaune), len(bleu)))

for i in range(len(jaune)):
    for j in range(len(bleu)):
        matrix[i][j] = jaune[i] + bleu[j]

#energy_values = matrix.reshape(-1, )

#### WORK IN PROGRESS ####
# On construit toutes les matrices binaires possibles de paires (jaune, bleu)
liste_jaune = list(permutations(range(len(jaune))))
liste_bleu = list(permutations(range(len(bleu))))

identity = np.eye(len(jaune), len(bleu))


result = 0

for k in range(len(jaune)):
    for l in range(len(bleu)):
        stochastic_matrix = identity[list(liste_jaune[k])][list(liste_bleu[l])]
        new_energy_values = np.multiply(matrix, stochastic_matrix)

        energy_values = new_energy_values.reshape(-1, )

        # On va appliquer l'algorithme de résolution du problème du sac à dos !!
        # /!\ L'algo du sac à dos s'applique avec une contrainte sur le weight, alors qu'ici on a une contrainte sur la valeur!!
        # Il faut sûrement en utiliser plutôt une variante...
        n = len(energy_values)
        tableau = np.zeros((n, Q))

        tableau[0, :] = energy_values[0] * np.ones((1, Q))
        for i in range(1, n):
            for j in range(Q):
                tableau[i, j] = max(energy_values[i] + tableau[i-1, j-1], tableau[i-1, j])

        result = max(result, tableau[-1, -1])

print(result)