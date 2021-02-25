import yfinance as yf
import streamlit as st
from datetime import date

st.write("""
# Gamestop stock price
![roaring kitty](https://i.imgur.com/bE2LMGd.gif "DFV likes the stock")

💎🙌🚀🚀🚀💎🙌
""")

current_date = date.today()

#define the ticker symbol
tickerSymbol = 'GME'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
tickerDf = tickerData.history(period='1d', start='2020-12-01', end=current_date)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
