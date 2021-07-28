import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

def read_nums_from_file(file, num):
    nums = []
    for line in file:
        nums.append([num(x) for x in line.split()])
    
    return nums
    

resp = open("resp03.txt")
itens = open("itens.txt")

resp_nums = read_nums_from_file(resp, int)
itens_nums = read_nums_from_file(itens, float)

num_aluno = 498

''' 
resp_nums: 500 linhas == 500 alunos
           45 colunas = 45 questões pra cada aluno

itens_nums: 45 linhas == 45 parâmetros abc 
            3 colunas == A, B e C
'''
#################################################################################

def likelihood(theta):
    sum_log = 0.0
    
    for i in range(len(resp_nums[0])):
        aux = .0
        if resp_nums[num_aluno][i] == 1: 
            aux = func_prob(itens_nums[i][0], itens_nums[i][1], itens_nums[i][2], theta)

        else:
            aux = 1 - func_prob(itens_nums[i][0], itens_nums[i][1], itens_nums[i][2], theta)

        sum_log += math.log(aux)
        
    return sum_log


def derivative(func, x):

    h = .00000001
    der = (func(x+h) - func(x)) / h
    return der


def func_prob(a, b, c, theta):

    exp_expression = math.e**(a*(theta-b))
    return c + ((1 - c) * (exp_expression / (1 + exp_expression)))


# def gradiente_f():

#     t = 0
#     t_old = t
#     beta = .001

#     for _ in range(30):

#         t = t + (beta * derivative(likelihood, t))

#         if likelihood(t) > likelihood(t_old):
#             beta *= 2
#             t_old = t
#         else: 
#             beta /= 2
#             t = t_old
        
#     return t


def gradiente_f():

    t = 0
    t_array = [t]
    beta = 0.2
    
    while t < 70:
        t+=1
        t_array.append(t)
        t_old = t
        t = t + (beta * derivative(likelihood, t))

        if likelihood(t_old) > likelihood(t) :
            beta *= 2
            t = t_old
        else: 
            beta /= 2
        
    plt.scatter(t_array, list(range(len(t_array))))
    plt.plot(list(range(len(t_array))), t_array)
    plt.savefig("graficoSerio.png")
        
    return t

print(gradiente_f())

# plt.scatter(theta, quant_acertos)
# plt.savefig("teste.png")
# quant_acertos = []
# thetas = []

# for i in range(len(resp_nums)):
#     quant_acertos.append(resp_nums[i].count(1))
    

# for i in range(len(resp_nums)):
#     num_aluno = i
#     theta = gradiente_f()
#     print(f"Aluno {i}\tTheta {theta}")
#     thetas.append(theta)

# plt.title("Gráfico de dispersão TRI")
# plt.scatter(thetas, quant_acertos)
# plt.xlabel('θ') 
# plt.ylabel('Acertos')
# plt.savefig("dispersao08.png")