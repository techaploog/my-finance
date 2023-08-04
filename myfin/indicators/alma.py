import pandas as pd
import numpy as np
from .indicator import Indicator

class ALMA(Indicator):
    def __init__(self, period:int=9, sigma:int=6, offset:float=0.85, column:str="Close"):
        self.column = column
        self.period = period
        self.sigma = sigma
        self.offset = offset if offset > 0 and offset < 1 else 0.85
        self.weight = self.set_weight()
        self.norm = sum(self.weight)
        self.desc = "ALMA_{}".format(self.period)

    def apply(self,serie:pd.Series | pd.DataFrame, column:str=None):
        column = column if column is not None else self.column

        data = super().get_df(serie,column)
        
        if data is None:
            return None
        
        data[self.desc] = data.rolling(self.period).apply(self.calculate_alma)

        return data[self.desc]
    
    def calculate_alma(self,serie:list):
        price = np.array(serie)
        return float(price.dot(self.weight)/self.norm)
    
    def set_weight(self):
        adj_offset = int(self.offset*(self.period - 1))
        smooth = self.period / self.sigma
        w = [np.exp(-((w_i-adj_offset)**2)/(2*(smooth**2))) for w_i in range(self.period)]
        return np.array(w)
    
    def __str__(self):
        return self.desc
