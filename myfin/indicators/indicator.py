from abc import ABC, abstractclassmethod

class Indicator(ABC):

    @abstractclassmethod
    def apply(self):
        pass