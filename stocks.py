import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import datetime
import yfinance as yf
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator


# DASHBOARD HEADERS AND TITLES#
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title('Stock Prices')
st.markdown('Based on stocks from [*Kiplinger 22 Stocks for 2022*](https://www.kiplinger.com/investing/stocks/stocks-to-buy/603893/22-best-stocks-to-buy-for-2022)')



# SIDEBAR #
st.sidebar.header('Choose A Stock')
stocklist = st.sidebar.selectbox('Select one symbol', ( 'DIS', 'UBER','QUASX','IAC', 'DXC', 'BABA', 'LFUS', 'SCHW', 'ABC', 'FAGAX', 'AGK', 'OGK', 'AMZN', 'PSA', 'BAC', 'CVS', 'SBUX', 'CCI', 'TROW', 'CVX', 'O', 'EPR'))
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
s1 = start_date.strftime("%d %B %Y")
end_date = st.sidebar.date_input('End date', today)
e1 = end_date.strftime("%d %B %Y")
st.sidebar.header('Displaying:')
if start_date < end_date:
    st.sidebar.success('Start date:  `%s`\n\nEnd date:  `%s`' % (s1, e1))
else:
    st.sidebar.error('Error: End date must fall after start date.')




stock_ticker = yf.Ticker(stocklist)
stock_info = stock_ticker.info
stock_name = stock_info["shortName"]
df = yf.download(stocklist,start= start_date,end= end_date, progress=False)
