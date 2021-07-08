import math 
#from math import e, log

a = [5, 1]
b = [2, -2]
x = [1, 0]

def derivative(f, x):
    # h = sys.float_info.min
    h = .0001
    der = (f(x+h) - f(x)) / h
    return der

def f(a, b, theta):

    exp_expression = math.e**(a*(theta-b))
    return (exp_expression / (1 + exp_expression))

def likelihood(theta):
    sum_log = 0.0
    
    for i in range(len(x)):
        aux = .0
        if x[i] == 1: 
            aux = f(a[i], b[i], theta)

        else:
            aux = 1.0 - f(a[i], b[i], theta)
            
        # print(type(math.log(aux, 10)))
        # print(type(aux))
        sum_log += math.log(aux)
        
    return sum_log
 #  linhas: 54 41 26


def gradiente_f():

    t = 0
    t_old = t
    beta = .001

    for _ in range(1000):

        t = t + (beta * derivative(likelihood, t))

        if likelihood(t) > likelihood(t_old):
            beta *= 2
            t_old = t
        else: 
            beta /= 2
            t = t_old
        
    return t



print(gradiente_f())




