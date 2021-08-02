from RandomVariable import RandomVariable

def expected_value(random_variable: RandomVariable, comp_func, *args) -> float:
    exp = 0.0

    for possible_value in random_variable.possible_values:
        exp += comp_func(possible_value, *args) * \
            random_variable.pdf(possible_value, *args)

    return exp    