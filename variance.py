def variance(possible_values_set, pdf, *args):

    from expected_value import expected_value

    exp0 = expected_value(set(x**2 for x in possible_values_set), pdf, *args)
    exp1 = expected_value(possible_values_set, pdf, *args)

    return (exp0 - (exp1 ** 2))

