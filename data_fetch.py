import yfinance as yf
import pandas as pd
import numpy as np
import datetime


target_tickers = ["CELH", "CVNA","UPST","ALT","FUBO"] 
start_data = datetime.datetime(2021, 1, 1)
end_data = datetime.datetime(2025, 1, 31)

tickers = yf.Tickers(" ".join(target_tickers))

data = yf.download(" ".join(target_tickers), start=start_data, end=end_data, group_by='ticker', threads=True)

for ticker in target_tickers:
    data[ticker].to_csv(f"data/{ticker}_{start_data}_{end_data}.csv")