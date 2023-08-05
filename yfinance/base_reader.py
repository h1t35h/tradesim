# import yfinance as yf 
# nifty_top = yf.Ticker("^NSEI")
# print(nifty_top._data)
# print(nifty_top._data.get_json_data_stores('components'))


import yahooquery as yq

nsei_index = yq.Ticker("^NSEI")