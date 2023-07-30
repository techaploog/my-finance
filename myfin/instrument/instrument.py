import yfinance as yfin

class Instrument:
    def __init__(self,symbol, indicators = [], period="1mo", freq="1d", **kwarg):
        self.symbol = symbol
        self.ticker = yfin.Ticker(symbol);
        self.indicators = indicators if type(indicators) == list else [indicators]
        self.period = period
        self.freq = freq
        self.start = kwarg["start"]
        self.end = kwarg["end"]
        self.data = None

    def load_data(self):
        options = {
            "period":self.period,
            "interval":self.freq,
            "start":self.start,
            "end":self.end
        }
        self.data = self.ticker.history(**options)

    def apply_indicators(self):
        # TODO: apply indicators to data
        for ind in self.indicators:
            pass