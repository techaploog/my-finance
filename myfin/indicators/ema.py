from .indicator import Indicator

datatype = {
    "data":list
}

class EMA(Indicator):
    def __init__(self,period):
        self.period = period

    def apply(self,data):
        # TODO: implement this function
        pass

    def __name__(self):
        return "EMA_{period}".format(period=self.period)