from .indicator import Indicator

class SMA(Indicator):
    def __init__(self,period):
        self.period = period

    def apply(self):
        pass

    def __str__(self):
        return "SMA_{period}".format(period=self.period)