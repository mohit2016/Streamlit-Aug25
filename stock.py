import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyzer.")



col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input("Which stock you want to analyse", "MSFT")
    ticker_data = yf.Ticker(ticker)
    
with col2:
    sd = st.date_input("Please enter Starting Date", datetime.date(2024, 8, 5))

with col3:    
    ed = st.date_input("Please enter Ending Date", datetime.date(2025, 8, 5))


ticker_df = ticker_data.history(start = sd, end=ed)

st.subheader("Here is the raw day wise stock price.")
st.dataframe(ticker_df.head())

st.subheader("Price movement over time")
st.line_chart(ticker_df['Close'])

st.subheader("Volume movement over time")
st.bar_chart(ticker_df['Volume'])