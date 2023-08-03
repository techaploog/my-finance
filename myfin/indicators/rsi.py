import pandas as pd
from .indicator import Indicator

class RSI(Indicator):
    def __init__(self,period:int=14, column:str="Close"):
        self.period = period
        self.column = column
        self.desc = "RSI_{period}".format(period=self.period)

    def apply(self,serie:pd.Series | pd.DataFrame, column:str=None):
        column = column if column is not None else self.column

        data = super().get_df(serie,column)
        
        if data is None:
            return None
        
        data["change"] = data[column].diff()
        data["loss"] = data["change"].map( lambda diff : abs(diff) if diff < 0 else 0.0)
        data["change"] = data["change"].abs()
        data["sum_loss"] = data["loss"].rolling(self.period,min_periods=self.period).sum()
        data["sum_change"] = data["change"].rolling(self.period,min_periods=self.period).sum()
        data[self.desc] = 1 - (data["sum_loss"]/data["sum_change"])
        data[self.desc] = data[self.desc] * 100

        return data[self.desc]
    
    def __str__(self):
        return self.desc
    

# * REFERENCE
"""
RSI = 100 - ( 100 / (1 + (AvgGain/AvgLoss)) )
    = 100 - ( 100 * (1 / ( 1 + (AvgGain/AvgLoss) )))
    = 100 - ( 100 * (1 / ( (AvgLoss/AvgLoss) + AvgGain/AvgLoss) )))
    = 100 - ( 100 * (1 / ( (AvgLoss + AvgGain) / AvgLoss) )))
    = 100 - ( 100 * (1 * ( AvgLoss/AvgChange ) )) , where AvgChange = AvgLoss + AvgGain
    = 100 - ( 100 * ( sum(Loss)/sum(Change) )) , because : sum(Loss)/N * N/sum(Change)
    = 100 * (1 - sum(Loss) / sum(Change) )
"""

# PS:
# With this derived equation, we can improve computational performance.
# Changin from rolling mean which need execute "divide" operation many times
# into rolling sum, use only "add" operation.