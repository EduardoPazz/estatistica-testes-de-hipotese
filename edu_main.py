def read_nums_from_file(file, num):
    nums = []
    for line in file:
        nums.append([num(x) for x in line.split()])
    
    return nums

resp = open("resp03.txt")
itens = open("itens.txt")

resp_nums = read_nums_from_file(resp, int)
items_nums = read_nums_from_file(itens, float)

questions_pdfs = list()

for abc in items_nums:
    a = abc[0]
    b = abc[1]
    c = abc[2]

    from pdf import PDF
    questions_pdfs.append(PDF(a, b, c))

from likelihood import Likelihood

lh = Likelihood(questions_pdfs)

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()

ax.plot(x, lh.get_log_likelihood(x))

plt.savefig("mygraph.png")
