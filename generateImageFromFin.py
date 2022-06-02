# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:12:53 2022

@author: Ballerina
"""

import pandas as pd
import yfinance as yf
import numpy as np
from PIL import Image

# Request historical data for past year
# Codes here: https://finance.yahoo.com/lookup?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADWHxWef5zP0hg1AoYXQmoB6TRg0r0-ealt8bOCh26cWzJ9sqQQjgxKni-4Vw3nV5Qx00TEFwO64TRdAZ1VG_BmBN5a1KC-2RcFym1v81e1Wg1FpavrWkifT30ROV7_MToBet7ULCSCTKIc4WFFIBUbgnDlWJvwdrcu3BL5lgBbi
data = yf.Ticker("NVDA").history(period='512d')
# Show info
#print(data.info())

im = Image.new("RGB", (512,512))
im = np.array(im)


for r in range(0,512):
    for c in range(0,512):
        #print( data['Open'][r], data['Close'][c], data['High'][r] )
        re = data['Open'][r]
        gr = data['Close'][c]
        bl = data['High'][r]#365#data['Close'][r]
        im[r][c]=[re,gr,bl]
img = Image.fromarray(im, 'RGB')
img.show()
img.save("randomFin.jpeg");