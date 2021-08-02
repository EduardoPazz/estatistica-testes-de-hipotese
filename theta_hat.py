from Question import question_list
from expected_value import expected_value
from variance import variance
from fisher_information import fisher_information
from statistics import NormalDist
from math import sqrt
from thetas import thetas

def calculate_expected_value_and_variance(theta: float) -> float:
    exp = theta
    total_fisher_info = 0.0

    for question in question_list:
        total_fisher_info += fisher_information(question, theta)

    var = 1 / total_fisher_info    

    return exp, var

theta_0A = 0
theta_0B = 2

exp = 0.0
var = 0.0

exp, var = calculate_expected_value_and_variance(theta_0A)
l_A = exp + (-1.645 * sqrt(var))

exp, var = calculate_expected_value_and_variance(theta_0B)
l_B = exp + (-1.645 * sqrt(var))

prob_A = list()
prob_B = list()

for theta in thetas:
    exp, var = calculate_expected_value_and_variance(theta)
    prob_A.append(NormalDist(0, 1).cdf((l_A - exp) / sqrt(var)))
    prob_B.append(NormalDist(0, 1).cdf((l_B - exp) / sqrt(var)))
