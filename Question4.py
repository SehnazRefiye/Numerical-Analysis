# Refiye Şehnaz Yıldırım - 171805012
# Ersu Karpuz - 171805043

def f(x):
    return x ** 2


# Implementing Simpson's 1/3
def simpson13(a, b, n):
    # calculating step size
    h = (b - a) / n

    # Finding sum
    integration = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(x)
        else:
            integration = integration + 4 * f(x)

    # Finding final integration value
    integration = h / 3 * integration

    return integration


for i in range(0, 3):
    lower_limit = 0
    upper_limit = 1

    print("Lower limit of integration: ", lower_limit)
    print("Upper limit of integration: ", upper_limit)

    if i == 0:
        sub_interval = 2
        result = simpson13(lower_limit, upper_limit, sub_interval)
        print("Number of sub intervals: ", sub_interval)
    elif i == 1:
        sub_interval = 4
        result = simpson13(lower_limit, upper_limit, 4)
        print("Number of sub intervals: ", sub_interval)
    else:
        sub_interval = 6
        result = simpson13(lower_limit, upper_limit, 6)
        print("Number of sub intervals: ", sub_interval)

    print("Integration result by Simpson's 1/3 method is: %0.4f" % result)
    print()
