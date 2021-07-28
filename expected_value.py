def expected_value(possible_values_set, pdf, *args) -> float:
    exp = 0.0

    for possible_value in possible_values_set:
        exp += possible_value * pdf(possible_value, *args)

    return exp    