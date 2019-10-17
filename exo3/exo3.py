import math

xb, yb = map(float, input().split(" "))
N, T = map(int, input().split(" "))

noms = ['']*N
x = dict()
y = dict()

for i in range(N):
    noms[i] = input()
    x[i] = [0]*T
    y[i] = [0]*T
    for j in range(T):
        x[i][j], y[i][j] = map(float, input().split(" "))


x_0 = dict(x)
y_0 = dict(y)

# for i in range(N):
#     for j in range(T):
#         x_0[i][j] = x_0[i][j] - xb
#         y_0[i][j] = y_0[i][j] - yb

resultat = ''
liste_noms = []
for i in range(N):
    possible = False
    possible_nom = False
    while not possible:
        for t in range(T-1):
            dist = math.sqrt((x[i][t+1] - xb)**2 + (y_0[i][t+1] - yb)**2) + math.sqrt((x[i][t] - xb)**2 + (y_0[i][t] - yb)**2)
            if dist <= 100:
                possible = True
                possible_nom = True
        possible = True

    if possible_nom:
        liste_noms.append(noms[i])

print (' '.join(liste_noms))

