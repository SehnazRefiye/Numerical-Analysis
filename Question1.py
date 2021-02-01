import numpy as np

# x coordinates in space
x = np.array([-2, 0, 1, 3], float)
# f(x)
y = np.array([8, 4, 2, -2], float)


def NDDI(x, y):
    n = np.shape(y)[0]
    # Create a square matrix to hold pyramid
    pyramid = np.zeros([n, n])
    # first column is y
    pyramid[::, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            # create pyramid by updating other columns
            pyramid[i][j] = (pyramid[i + 1][j - 1] - pyramid[i][j - 1]) / (x[i + j] - x[i])
    # return first row
    return pyramid[0]


result = NDDI(x, y)
print(result)

# create as many polynomials as size of result
# our target polynomial
final_pol = np.polynomial.Polynomial([0.])
# get number of result
n = result.shape[0]
for i in range(n):
    # create a dummy polynomial
    p = np.polynomial.Polynomial([1.])
    for j in range(i):
        # each vector has degree of i
        # their terms are dependant on 'x' values
        # (x - x_j)
        p_temp = np.polynomial.Polynomial([-x[j], 1.])
        # multiply dummy with expression
        p = np.polymul(p, p_temp)
    # apply coefficient
    p *= result[i]
    # add to target polynomial
    final_pol = np.polyadd(final_pol, p)

p = np.flip(final_pol[0].coef, axis=0)
print(p)
print(np.poly1d(p))
# print("P(x) =", int(p[0]), "x + ", int(p[1]))
