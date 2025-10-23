import streamlit as st
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import pandas as pd
import mplfinance as mpf
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"

st.title("Welcome to 'Kalakal' Trading Company")
st.write('This is the best trading company from Philippines')
st.markdown("*Kalakal* is **a Great** ***Trading Company!***.")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh5Mj57Qmv0spaHz01IqRvpmQPq6cS6sG9Wg&s")

multi = '''If you want to learn more about Kalakal,

I will tell about it later, but first see the graph and table below:
'''
st.markdown(multi)
# Specify title and logo for the webpage.
# Set up your web app
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input")
symbol = st.sidebar.text_input('Stock symbol: ', 'NVDA').upper()
ma1 = st.sidebar.slider('Short-term moving average days: ',min_value=10, max_value=100, step=10)
ma2 = st.sidebar.slider('Long-term moving average days: ',min_value=50, max_value=200, step=10)
# Selection for a specific time frame.
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date',value=datetime.date(2021,1,1))
with col2:
    edate = st.date_input('End Date',value=datetime.date.today())


st.title(f"Symbol : {symbol}")

stock = yf.Ticker(symbol)
if stock is not None:
  # Display company's basics
  st.write(f"# Name : {stock.info['shortName']}")
  st.write(f"# Market : {stock.info['market']}")
else:
  st.error("Failed to fetch historical data.")

data = yf.download(symbol,start=sdate,end=edate,multi_level_index=False,auto_adjust=False)
if data is not None:
    fig, ax = mpf.plot(data,type='candle',style='yahoo',mav=(ma1,ma2),volume=True,returnfig=True)
    st.pyplot(fig)
else:
    st.error("Failed to fetch historical data.")
