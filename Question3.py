import numpy as np

# x
a = np.array([2.36, 2.37, 2.38, 2.39])
# f(x)
b = np.array([0.85866, 0.86289, 0.86710, 0.87129])

x = 2.38
h = 0.01


# define the function
def function(x):
    return -0.1*x**2 + 0.896*x-0.69894


upper = function(x + h)
lower = function(x - 2*h)


# forward difference first derivative O(h**2)
def forward_1(function, x, h, upper, lower):
    if lower <= function(x + 2*h) <= upper:
        if lower <= function(x + h) <= upper:
            if lower <= function(x) <= upper:
                f = (- function(x + 2*h) + 4*function(x + h) - 3*function(x)) / (2 * h)
                return f
            else:
                c = "It cannot be calculated!"
                return c
        else:
            c = "It cannot be calculated!"
            return c
    else:
        c = "It cannot be calculated!"
        return c
    # f = (- function(x + 2*h) + 4*function(x + h) - 3*function(x)) / (2 * h)
    # return f


# forward difference second derivative O(h**2)
def forward_2(function, x, h, upper, lower):
    if lower <= function(x + 3*h) <= upper:
        if lower <= function(x + 2*h) <= upper:
            if lower <= function(x + h) <= upper:
                if lower <= function(x) <= upper:
                    f = (- function(x + 3*h) + 4*function(x + 2*h) - 5*function(x + h) + 2*function(x)) / h**2
                    return f
                else:
                    c = "It cannot be calculated!"
                    return c
            else:
                c = "It cannot be calculated!"
                return c
        else:
            c = "It cannot be calculated!"
            return c
    else:
        c = "It cannot be calculated!"
        return c
    # f = (- function(x + 3*h) + 4*function(x + 2*h) - 5*function(x + h) + 2*function(x)) / h**2
    # return f
    

# backward difference first derivative O(h**2)
def backward_1(function, x, h, upper, lower):
    if lower <= function(x) <= upper:
        if lower <= function(x - h) <= upper:
            if lower <= function(x - 2*h) <= upper:
                f = (3*function(x) - 4*function(x - h) + function(x - 2*h)) / (2 * h)
                return f
            else:
                c = "It cannot be calculated!"
                return c
        else:
            c = "It cannot be calculated!"
            return c
    else:
        c = "It cannot be calculated!"
        return c
    # f = (3*function(x) - 4*function(x - h) + function(x - 2*h)) / (2 * h)
    # return f


# backward difference second derivative O(h**2)
def backward_2(function, x, h, upper, lower):
    if lower <= function(x) <= upper:
        if lower <= function(x - h) <= upper:
            if lower <= function(x - 2*h) <= upper:
                if lower <= function(x - 3*h) <= upper:
                    f = (2*function(x) - 5*function(x - h) + 4*function(x - 2*h) - function(x - 3*h)) / h**2
                    return f
                else:
                    c = "It cannot be calculated!"
                    return c
            else:
                c = "It cannot be calculated!"
                return c
        else:
            c = "It cannot be calculated!"
            return c
    else:
        c = "It cannot be calculated!"
        return c
    # f = (2*function(x) - 5*function(x - h) + 4*function(x - 2*h) - function(x - 3*h)) / h**2
    # return f


# central difference first derivative O(h**2)
def central_1(function, x, h, upper, lower):
    if lower <= function(x + h) <= upper:
        if lower <= function(x - h) <= upper:
            f = (function(x + h) - function(x - h)) / (2 * h)
            return f
        else:
            c = "It cannot be calculated!"
            return c
    else:
        c = "It cannot be calculated!"
        return c
    # f = (function(x + h) - function(x - h)) / (2 * h)
    # return f


# central difference second derivative O(h**2)
def central_2(function, x, h, upper, lower):
    if lower <= function(x + h) <= upper:
        if lower <= function(x) <= upper:
            if lower <= function(x - h) <= upper:
                f = (function(x + h) - 2*function(x) + function(x - h)) / h**2
                return f
            else:
                c = "It cannot be calculated!"
                return c
        else:
            c = "It cannot be calculated!"
            return c
    else:
        c = "It cannot be calculated!"
        return c
    # f = (function(x + h) - 2*function(x) + function(x - h)) / h**2
    # return f


exact = -0.2*x + 0.896
dydt_f1 = forward_1(function, x, h, upper, lower)
dydt_f2 = forward_2(function, x, h, upper, lower)
dydt_b1 = backward_1(function, x, h, upper, lower)
dydt_b2 = backward_2(function, x, h, upper, lower)
dydt_c1 = central_1(function, x, h, upper, lower)
dydt_c2 = central_2(function, x, h, upper, lower)


print("Exact value = %0.2f" % exact)
print("Forward Difference f'(2.38) = ", dydt_f1)
print("Forward Difference f''(2.38) = ", dydt_f2)
print("Backward Difference f'(2.38) = %0.2f" % dydt_b1)
print("Backward Difference f''(2.38) = ", dydt_b2)
print("Central Difference f'(2.38) = %0.2f" % dydt_c1)
print("Central Difference f''(2.38) = %0.1f" % dydt_c2)

