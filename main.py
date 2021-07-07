from log_likelihood import question_function
#import matplotlib.pyplot as plt

def read_nums_from_file(file, num):
    nums = []
    for line in file:
        nums.append([num(x) for x in line.split()])
    
    return nums
'''
def plot_grafico():

    plt.plot(x, y)

def plot_dispersao():
    fig = plt.figure()
    ax1 = fig.add_subplot(121)

'''

resp = open("resp03.txt")
itens = open("itens.txt")

resp_nums = read_nums_from_file(resp, int)
itens_nums = read_nums_from_file(itens, float)

maximuns = list()
minimuns = list()


for row in itens_nums:
    theta = -15.0
    probs = list()
    while theta <= 5.0:
        probs.append(question_function(row[0], row[1], row[2], theta))
        theta += .1
    
    maximuns.append(max(probs))
    minimuns.append(min(probs))
tob
print("Maximuns:")
print(maximuns)

print("Minimuns:")
print(minimuns)