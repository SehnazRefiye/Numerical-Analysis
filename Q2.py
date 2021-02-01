import numpy as np

matrixA = np.array([[2, -3, -1],
                    [3, 2, -5],
                    [2, 4, -1]], float)
matrixB = np.array([[3],
                    [-9],
                    [-5]], float)

print('A =\n', matrixA)
print('\nB =\n', matrixB)

n = len(matrixB)
x = np.zeros(n, float)

for i in range(n-1):
    for j in range(i+1, n):
        esi = matrixA[j][i] / matrixA[i][i]
        for k in range(i, n):
            matrixA[j][k] = matrixA[j][k] - esi * matrixA[i][k]
        matrixB[j] = matrixB[j] - matrixB[i] * esi
print('\nAfter applying the gauss elimination method A =\n', matrixA)
print('\nAfter applying the gauss elimination method B =\n', matrixB)

x[n-1] = matrixB[n-1] / matrixA[n-1][n-1]
for i in range(n-2, -1, -1):
    gauss_sum = 0
    for j in range(i+1, n):
        gauss_sum = gauss_sum + matrixA[i][j] * x[j]
    x[i] = (matrixB[i] - gauss_sum) / matrixA[i][i]

print()
for i in range(n):
    print('X%d = %0.2f' % (i+1, x[i]), end='\t')
