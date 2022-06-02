# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:46:30 2022

@author: Ballerina
"""

#pip3 install yfinance

import pandas as pd
import yfinance as yf

# Request historical data for past 5 years
data = yf.Ticker("NVDA").history(period='5y')
# Show info

print(data.info())
print(data)
print(data['Close'])