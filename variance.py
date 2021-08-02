from RandomVariable import RandomVariable

def variance(random_variable: RandomVariable, *args) -> float:

    from expected_value import expected_value

    exp0 = expected_value(random_variable, lambda *args: args[0] ** 2, *args)
    exp1 = expected_value(random_variable, lambda *args: args[0], *args)

    return (exp0 - (exp1 ** 2))

