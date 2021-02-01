from numpy import array, dot, zeros

def dlt(matrixA):
    n = len(matrixA)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if matrixA[i, k] != 0.0:
                factor = matrixA[i, k] / matrixA[k, k]
                matrixA[i, k + 1:n] -= matrixA[k, k + 1:n] * factor
                matrixA[i, k] = factor
    return matrixA

def Doolittles_Decomposition(matrixA, matrixB):
    n = len(matrixB)
    for k in range(1, n):
        matrixB[k] -= dot(matrixA[k, 0:k], matrixB[0:k])
    matrixB[n - 1] /= matrixA[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        matrixB[k] = (matrixB[k] - dot(matrixA[k, k + 1:n], matrixB[k + 1:n])) / matrixA[k, k]
    return matrixB


matrixA = array([[2.34, -4.10, 1.78], [-1.98, 3.47, -2.22], [2.36, -15.17, 6.18]], float)

matrixB = array([[0.02], [-0.73], [-6.63]], float)

print('A =\n', matrixA)
print('\nB =\n', matrixB)
print()

dlt(matrixA)
X = Doolittles_Decomposition(matrixA, matrixB)
n = len(matrixB)
for i in range(n):
    print('X%d = %g' % (i+1, X[i]), end='\t')
