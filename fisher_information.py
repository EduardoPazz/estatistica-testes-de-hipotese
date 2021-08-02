from RandomVariable import RandomVariable
from expected_value import expected_value

def fisher_information(random_variable: RandomVariable, *args) -> float:
    return expected_value(random_variable, \
        lambda *args: random_variable.derivative_log_likelihood(*args) ** 2, \
        *args)