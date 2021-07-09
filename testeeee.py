# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# # plt.show()


plt.scatter([1,2,3], [4,8,1])
plt.savefig("teste.png")

# %%

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

''' 
resp_nums: 500 linhas == 500 alunos
           45 colunas = 45 questões pra cada aluno

itens_nums: 45 linhas == 45 parâmetros abc 
            3 colunas == A, B e C
'''


def derivative(fun, x, j):
    h = .0001
    der = (fun(x+h, j) - fun(x, j)) / h
    return der

def f(a, b, c, theta):

    exp_expression = math.e**(a*(theta-b))
    return c + ((1 - c) * (exp_expression / (1 + exp_expression)))

def likelihood(theta, j):
    sum_log = 0.0
    
    for i in range(len(resp_nums[j])):
        aux = .0
        if resp_nums[j][i] == 1: 
            aux = f(itens_nums[i][0], itens_nums[i][1], itens_nums[i][2], theta)

        else:
            aux = 1 - f(itens_nums[i][0], itens_nums[i][1], itens_nums[i][2], theta)
        
        print("aux: ", aux)
        sum_log += math.log(aux)
        
    return sum_log

def gradiente_f(j):

    t = 0
    t_old = t
    beta = .001

    for _ in range(10):

        t = t + (beta *  derivative(likelihood, t, j))

        if likelihood(t, j) > likelihood(t_old, j):
            beta *= 2
            t_old = t
        else: 
            beta /= 2
            t = t_old
        
    return t

#print(gradiente_f())

quant_acertos = []

for i in range(len(resp_nums)):
    quant_acertos.append(resp_nums[i].count(1))
    
thetas = []

for i in range(len(resp_nums)):
    thetas.append(gradiente_f(i))

print(thetas)
plt.scatter(thetas, quant_acertos)
plt.savefig("dispersao03.png")
