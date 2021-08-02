from Question import question_list
from expected_value import expected_value
from variance import variance
from statistics import NormalDist
from math import sqrt
from thetas import thetas

def calculate_expected_value_and_variance(t):
    exp = 0.0
    var = 0.0
    for question in question_list:
        exp += expected_value(question, lambda *args: args[0], t)
        var += variance(question, t)

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
