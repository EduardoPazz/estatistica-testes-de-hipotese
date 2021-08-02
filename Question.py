from RandomVariable import RandomVariable

class Question(RandomVariable):
    def __init__(self, id: int, a: float, b: float, c: float):
        self.id = id
        self.a = a
        self.b = b
        self.c = c

    possible_values = (0, 1)

    def pdf(self, *args) -> float:
        if len(args) != 2:
            raise Exception("São necessários 2 argumentos: x e theta.")

        x = args[0]
        theta = args[1]

        from math import e

        e_expression = e ** (self.a * (theta - self.b))

        default_result = (self.c + ((1 - self.c) * (e_expression / (1 + e_expression))))

        if (x == 1):
            return default_result
        elif (x == 0):
            return (1 - default_result)
        else:
            raise Exception("'x' deve ser 1 ou 0.")


    def log_likelihood(self, *args) -> float:
        from math import log
        return log(self.pdf(*args))


    def derivative_log_likelihood(self, *args) -> float:
        h = .000001
        return ((self.log_likelihood(args[0], args[1] + h) - \
            self.log_likelihood(*args)) / h)


    def __str__(self):
        return f"{self.id}: {self.a} - {self.b} - {self.c}"


parameters_file = open("parametros.txt")

from read_nums_from_file import read_nums_from_file

parameters_matrix = read_nums_from_file(parameters_file, float)

question_list = list()
for i in range(len(parameters_matrix)):
    a = parameters_matrix[i][0]
    b = parameters_matrix[i][1]
    c = parameters_matrix[i][2]

    question_list.append(Question(i, a, b, c))

