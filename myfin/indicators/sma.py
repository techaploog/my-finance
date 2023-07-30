import pandas as pd
from .indicator import Indicator

class SMA(Indicator):
    def __init__(self,period,columns=["Close"]):
        self.period = period
        self.columns = columns
        self.desc = "SMA_{period}".format(period=self.period)

    def apply(self,serie:pd.Series | pd.DataFrame):
        data = serie[self.columns].copy()
        data = data.rolling(self.period).mean()
        data.columns = [self.desc]
        return data

    def __str__(self):
        return self.desc