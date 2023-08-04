import yfinance as yfin
import pandas as pd

class Instrument:
    def __init__(self,symbol:str, indicators = [], period="1mo", freq="1d", **kwarg):
        self.symbol = symbol
        self.ticker = yfin.Ticker(symbol);
        self.indicators = indicators if type(indicators) == list else [indicators]
        self.period = period
        self.freq = freq
        self.start = kwarg["start"] if "start" in kwarg.keys() else None
        self.end = kwarg["end"] if "end" in kwarg.keys() else None
        self.data = None
        print("[INFO] {} | freq : {}".format(self.symbol,self.freq))

    def load_data(self, apply_indictors = True):
        options = {
            "period":self.period,
            "interval":self.freq,
            "start":self.start,
            "end":self.end
        }
        self.data = self.ticker.history(**options)
        print("[INFO] {} | total data = {} row(s)".format(self.symbol,len(self.data)))

        if (apply_indictors):
            self.apply_indicators()


    def apply_indicators(self):
        for ind in self.indicators:
            print("[INFO] {} | apply : {}".format(self.symbol, str(ind)))
            res = ind.apply(self.data)
            self.data = pd.concat([self.data,res],axis=1)