from PDFQuestion import pdf_list
from expected_value import expected_value
from variance import variance

theta = 0
total_expected_value = 0.0
total_variance = 0.0

for pdf in pdf_list:
    total_expected_value += expected_value({0, 1}, pdf.apply, theta)
    total_variance += variance({0, 1}, pdf.apply, theta)


from statistics import NormalDist
from math import sqrt

sigma = sqrt(total_variance)

l = total_expected_value + (-1.645 * sigma)

prob = NormalDist(0, 1).cdf(-1.645)

print(l)

print(f"Pr(T <= {l} | theta={theta}) = {prob}")

# import matplotlib.pyplot as plt
# import numpy as np

# pdf = pdf_list[0]

# x = np.linspace(-10, 10, 100)

# for n in [1, 2]:
#     y = [ pdf.apply(1, i) * n for i in x ]
#     plt.plot(x, y)


# plt.savefig("test.png")