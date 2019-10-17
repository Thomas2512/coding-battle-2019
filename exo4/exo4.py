import math

q = int(input())
n = int(input())

jaune = [0] * (N/2)
bleu = [0] * (N/2)

for i in range(N/2):
    jaune[i] = int(str(input())[2:])

for i in range(N/2):
    bleu[i] = int(str(input())[2:])

maxi = 0

for i in range(N/2):
    for j in range(N/2):
        if jaune[i]+bleu[j] <= q:
            maxi = max(maxi, jaune[i]+bleu[j])

print (maxi)
