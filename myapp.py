import datetime
import yfinance as yf
import streamlit as st
import pandas as pd

def display(option, period, start, end):
    companies = {
        'Google':'GOOGL',
        'Apple':'AAPL',
        'Microsoft':'MSFT',
        'Meta':'Meta',
        'Tesla':'TSLA',
        'Amazone': 'AMZN'
    }
    tickerSymbol = companies[option]
    tickerData = yf.Ticker(tickerSymbol)
    st.write("""### """+option)
    st.write(tickerData.info['longBusinessSummary'])

    tickerDf = tickerData.history(period=period, start=start, end=end)
    st.write("""
    Shown is the stock **closing price** of
    """+option+""" from """,start,""" to """,end)
    st.line_chart(tickerDf.Close)
    st.write("""
    Shown is the stock **volume** of
    """+option+""" from """,start,""" to """,end)

    st.line_chart(tickerDf.Volume)

st.write("""
# Simple Stock Price App
""")

form = st.form("my_form")
# form.slider("Inside the form")
option = form.selectbox(
             'Which Company do you want to obseve stock related information?',
             ('Google', 'Apple', 'Microsoft', 'Meta', 'Tesla', 'Amazone'))
period = form.select_slider(
    'Select a frequency of data to display',
    options=['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'])
col1, col2 = form.columns(2)
start = col1.date_input(
    """Select the start date (format is yyyy-MM-dd)""",
    datetime.date(2010, 1, 1))
end = col2.date_input(
"""Select the end date (format is yyyy-MM-dd)""")
form.form_submit_button("Submit", on_click=display(option, period, start, end), args=(option, period, start, end))

