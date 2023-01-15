import datetime
import yfinance as yf
import streamlit as st

def display(option, period, start, end):
    """
        Displays stock data for the selected company, frequency of data, 
        and time period.
        
        Parameters:
        option (str): The name of the company.
        period (str): The frequency of data to display.
        start (datetime): The start date of the time period.
        end (datetime): The end date of the time period.
        
        Returns:
        None
    """

    companies = {
        'Google':'GOOGL',
        'Apple':'AAPL',
        'Microsoft':'MSFT',
        'Meta':'Meta',
        'Tesla':'TSLA',
        'Amazone': 'AMZN'
    }
    freq = {
        '1 min': '1m',
        '2 mins': '2m',
        '5 mins': '5m',
        '15 mins': '15m',
        '30 mins': '30m',
        '1h': '1h',
        '90 mins': '90m',
        '1 day': '1d',
        '5 days': '5d',
        '1 week': '1wk',
        '1 mo': '1mo',
        '3 mo': '3mo'

    }
    tickerSymbol = companies[option]
    tickerData = yf.Ticker(tickerSymbol)
    st.write("""### """+option)
    st.write("""#### Company presentation:""")
    st.write(tickerData.info['longBusinessSummary'])

    tickerDf = tickerData.history(period=freq[period], start=start, end=end)
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
option = form.selectbox(
             'Select the company you want to display stock data',
             ('Google', 'Apple', 'Microsoft', 'Meta', 'Tesla', 'Amazone'))
period = form.select_slider(
    'Select a frequency of data to display',
    options=['1 min','2 mins','5 mins','15 mins','30 mins','1h','90 mins','1 day','5 days','1 week','1 mo','3 mo'])
col1, col2 = form.columns(2)
start = col1.date_input(
    """Select the start date (format is yyyy-MM-dd)""",
    datetime.date(2010, 1, 1))
end = col2.date_input(
"""Select the end date (format is yyyy-MM-dd)""")
form.form_submit_button("Submit", on_click=display(option, period, start, end), args=(option, period, start, end))

