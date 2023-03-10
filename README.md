# Tech-companies-stock-price
## Overview
A simple web application to help stock enthusisasts track the stock price of some big tech companies within a period of their choice.
Our application enables to display information about the following firms:
* Google
* Apple
* Microsoft
* Meta
* Tesla
* Amazone
## Technologies
Our application is based on python and more specifically on :
* [`streamlit`](https://streamlit.io/): Is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes.
* [`yfinance`](https://pypi.org/project/yfinance/): Is a popular open source library to access the financial data available on [Yahoo Finance](https://finance.yahoo.com/). Yahoo Finance offers an excellent range of market data on stocks, bonds, currencies and cryptocurrencies. It also offers market news, reports and analysis and additionally options and fundamentals data- setting it apart from some of it’s competitors.
### Python version: 
Preferably python 3.9
## Required packages:
* streamlit==1.11.0
* yfinance==0.2.4
## Deployed version
You can visit the deployed version via [this link](https://ahmedbellaaj10-tech-companies-stock-price-myapp-ov72sg.streamlit.app/)
## Try it yourself
You can clone this repo on you local machine using:
```cmd
git clone https://github.com/ahmedbellaaj10/Tech-companies-stock-price.git
```
Then install the needed requirements using:
```cmd
pip install -r requirements.txt
```
To run the server you can type the following command:
```cmd
streamlit run myapp.py
```
A new window will pop-up in your browser displaying the following components:
### Form
As shown above, you can choose thanks to this form the company you want to study, the start and the end date, and the frequency of the displayed data.

![image](images/from.png)

### Company infos

As you submit, a detailed presentation of the company will be displayed.

![image](images/infos.png)

### Graphs
Depending on the choosen options in the form, two curves will be displayed: one tracking the evolution of the closing stock price and the other showing the stock volume of the choosing company.

![image](images/courbe.png)

The two curves are interactive: you can play around with them, zoom in, zoom out, use the mouse pointer to read a specific data point and especially save the image in different forms.

![image](images/interactive.png)

### Contributions and contact
I hope this simple project will help stock enthusiasts extract some data and use it in a practical way.
If you have any ideas to improve this work, you can contact me via mail on ```ahmed-bellaaj@outlook.com``` or via [linkedIn](https://www.linkedin.com/in/ahmed-bellaaj/).
Any feedback will be appreciated.
