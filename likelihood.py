class Likelihood:
    def __init__(self, questions_pdfs):
        self.questions_pdfs = questions_pdfs

    def get_log_likelihood(self, theta):
        from math import log
        from functools import reduce

        return reduce(lambda a, b: a + log(b.get_function(theta)), \
            self.questions_pdfs, 0)
