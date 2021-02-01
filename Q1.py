import numpy as np
from sympy import *

# Derivative
def Derivative_sin2x(n, a):
    x = Symbol('x')
    devsin2x = (sin(2*x).diff(x, n))
    return float((devsin2x).subs(x, a))

# Factorial
def fact(n):
    return 1 if (n == 1 or n == 0) else float(n * fact(n - 1))

step = []
total = 0
exact_value = sin(2*(np.pi/4))
x = np.pi/4

a = 0
for n in range(0, 5):
    formula = (Derivative_sin2x(n, a))/(fact(n))*((x-a)**n)
    total = total + formula
    step.append(total)

# Absolute Error
absolute_error = float(abs(exact_value - step[-1]))
print(str("Absolute Error: " + str(absolute_error)))

# Relative Error
relative_error = float(abs(exact_value - step[-1])/abs(exact_value))
print(str("Relative Error: " + str(relative_error)))

# Percentage Error
percentage_error = float(relative_error/exact_value*100)
print(str("Percentage Error: %" + str(percentage_error)))

