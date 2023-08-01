# my-finance : A simple investment tools

## Status : On Going ...
Having a good time in boths investing and coding :)

## Notices
Currently, this project rely on history data from `yfinance` as a data source.

Therefore, when working with other data source, all indicators classes need to init with a corresponding `column` parameter.

## Requirements
[Python](https://www.python.org/downloads/) : 3.^10

## A Simple guide
1. Download this repository 
```
git clone https://github.com/techaploog/my-finance.git
```

2. Create and activate your `python` [environment](https://docs.python.org/3/library/venv.html).

3. Install all requirements
```
pip install -r requirements.txt
```

## Example
```
from myfin.instrument import Instrument
from myfin.indicators import SMA,EMA, MACD, RSI

symbol = "EURUSD=X"
start = "2022-01-01"

sma20 = SMA(20)
ema50 = EMA(50)
macd = MACD()
rsi = RSI()

eur_usd = Instrument(symbol=symbol,start=start,indicators=[sma20,ema50,macd,rsi])
eur_usd.load_data()

eur_usd.data[["Close","SMA_20","EMA_50"]].plot(figsize=(10,5))
```

