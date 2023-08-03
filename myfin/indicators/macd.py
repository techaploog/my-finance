import pandas as pd
from .indicator import Indicator
from .ema import EMA

class MACD(Indicator):
    def __init__(self,signal_period:int=9, ema_fast_period:int=12, ema_slow_period:int=26, column:str="Close"):
        self.column = column
        self.signal = signal_period
        self.ema_fast = ema_fast_period
        self.ema_slow = ema_slow_period
        self.desc = "MACD_{slow}/{fast}/{macd}".format(slow=self.ema_slow,fast=self.ema_fast,macd=self.signal)

    def apply(self,serie:pd.Series | pd.DataFrame, column:str=None):
        cal_column = column if column is not None else self.column

        data = super().get_df(serie,cal_column)
        
        if data is None:
            return None
        
        # calculation
        ema_fast = EMA(period=self.ema_fast, column=cal_column)
        ema_slow = EMA(period=self.ema_slow, column=cal_column)

        data["MACD_FAST"] = ema_fast.apply(data)
        data["MACD_SLOW"] = ema_slow.apply(data)
        data["MACD"] = data["MACD_FAST"] - data["MACD_SLOW"]

        signal = EMA(period=self.signal, column="MACD")
        data["MACD_SIGNAL"] = signal.apply(data)

        data = data.drop(columns=cal_column,axis=1)

        return data

    def __str__(self):
        return self.desc
    

#* REFERENCE : www.investopedia.com
"""
The moving average convergence/divergence (MACD, or MAC-D) line is calculated by 
subtracting the 26-period exponential moving average (EMA) from the 12-period EMA. 
The signal line is a nine-period EMA of the MACD line.

MACD is best used with daily periods, where the traditional settings of 26/12/9 days is the default.

MACD triggers technical signals when the MACD line crosses above the signal line (to buy) or falls below it (to sell).

MACD can help gauge whether a security is overbought or oversold, alerting traders to the strength of a directional move, 
and warning of a potential price reversal.

MACD can also alert investors to bullish/bearish divergences 
(e.g., when a new high in price is not confirmed by a new high in MACD, and vice versa), 
suggesting a potential failure and reversal.

After a signal line crossover, it is recommended to wait for three or four days to confirm that it is not a false move.
"""

