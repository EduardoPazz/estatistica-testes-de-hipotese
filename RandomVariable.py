from abc import ABC, abstractmethod, abstractproperty

class RandomVariable(ABC):

    @abstractproperty
    def possible_values(self):
        pass

    @abstractmethod
    def pdf(self, *args):
        pass

    @abstractmethod
    def log_likelihood(self, *args):
        pass
    @abstractmethod

    def derivative_log_likelihood(self, *args):
        pass






