import pandas as pd
from .indicator import Indicator
from .sma import SMA

class VolumeOscillator(Indicator):
    def __init__(self,fast_ma:int=14,slow_ma:int=28,column:str ="Volume"):
        self.fast_ma = fast_ma
        self.slow_ma = slow_ma
        self.column = column
        self.desc = "VO"

    def apply(self,serie:pd.Series | pd.DataFrame, column:str=None):
        column = column if column is not None else self.column
        
        data = super().get_df(serie,column)
        
        if data is None:
            return None

        # calculation
        fast = SMA(period=self.fast_ma,column=column)
        slow = SMA(period=self.slow_ma,column=column)

        data["fast"] = fast.apply(data)
        data["slow"] = slow.apply(data)
        data[self.desc] = (data["fast"] - data["slow"])/data["slow"]
        data[self.desc] = data[self.desc] * 100
        return data[[self.desc]]

    def __str__(self):
        return "VO_{fast}/{slow}".format(fast=self.fast_ma,slow=self.slow_ma)