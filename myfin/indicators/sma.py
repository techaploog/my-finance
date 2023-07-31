import pandas as pd
from .indicator import Indicator

class SMA(Indicator):
    def __init__(self,period:int,column:str ="Close"):
        self.period = period
        self.column = column
        self.desc = "SMA_{period}".format(period=self.period)

    def apply(self,serie:pd.Series | pd.DataFrame, column:str=None):
        data = None
        column = column if column is not None else self.column
        
        # handle params
        if (isinstance(serie,pd.Series)):
            data = serie.copy()
            data = pd.DataFrame(data)
        elif (isinstance(serie,pd.DataFrame)) :
            data = serie[[column]].copy()
        
        if data is None:
            return None

        # calculation
        data = data.rolling(self.period).mean()
        data.columns = [self.desc]
        return data

    def __str__(self):
        return self.desc