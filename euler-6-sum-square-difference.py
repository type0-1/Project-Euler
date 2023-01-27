import sys

n = int(sys.argv[1])
allSquare = []
indivSquare = []
total = 0

for i in range(1, n + 1):
    allSquare.append(i)
    total += (i ** 2)
print((sum(allSquare) ** 2) - total)