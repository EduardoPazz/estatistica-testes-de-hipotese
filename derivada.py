def derivada(func, x):

    h = .000001
    der = (func(x+h) - func(x)) / h
    return der