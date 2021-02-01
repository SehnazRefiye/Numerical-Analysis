# Refiye Şehnaz Yıldırım - 171805012
# Ersu Karpuz - 171805043


# Defining Function
def f(x):
    return 3 * x**3 + x**2 - x - 5


# Defining derivative of function
def fd(x):
    return 9 * x**2 + 2*x - 1


x0 = -1
e = 0.000001

# Implementing Newton Raphson Method
def newtonRaphson(x0, e):
    print('\nNEWTON RAPHSON METHOD IMPLEMENTATION')
    step = 1
    flag = 1
    condition = True

    while condition:
        x1 = x0 - f(x0)/fd(x0)
        print('Iteration-%d, x%d = %0.4f' % (step, step, x1))
        x0 = x1
        step = step + 1

        if fd(x0) == 0.0:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.4f' % x1)

newtonRaphson(x0, e)
