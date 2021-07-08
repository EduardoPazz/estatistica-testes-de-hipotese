#import matplotlib.pyplot as plt
import math

def read_nums_from_file(file, num):
    nums = []
    for line in file:
        nums.append([num(x) for x in line.split()])
    
    return nums
    
x = 0

'''
def plot_grafico():

    plt.plot(x, y)

def plot_dispersao():
    fig = plt.figure()
    ax1 = fig.add_subplot(121)

'''

resp = open("ie/resp03.txt")
itens = open("ie/itens.txt")

resp_nums = read_nums_from_file(resp, int)
itens_nums = read_nums_from_file(itens, float)

''' 
resp_nums: 500 linhas == 500 alunos
           45 colunas = 45 questões pra cada aluno

itens_nums: 45 linhas == 45 parâmetros abc 
            3 colunas == A, B e C
'''

# print(resp_nums)
# print(itens_nums)


def derivative(f, x):
    # h = sys.float_info.min
    h = .0001
    der = (f(x+h) - f(x)) / h
    return der

def f(a, b, c, theta):

    exp_expression = math.e**(a*(theta-b))
    return c + ((1 - c) * (exp_expression / (1 + exp_expression)))

def likelihood(theta):
    sum_log = 0.0
    
    for i in range(len(resp_nums[0])):
        aux = .0
        if resp_nums[3][i] == 1: 
            aux = f(itens_nums[i][0], itens_nums[i][1], itens_nums[i][2], theta)

        else:
            aux = 1 - f(itens_nums[i][0], itens_nums[i][1], itens_nums[i][2], theta)

        sum_log += math.log(aux)
        
    return sum_log



def gradiente_f():

    t = 10
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