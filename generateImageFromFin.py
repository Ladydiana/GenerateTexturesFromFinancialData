# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:12:53 2022

@author: Ballerina
"""

import pandas as pd
import yfinance as yf
import numpy as np
from PIL import Image
from datetime import datetime

# Request historical data for past year
# Codes here: https://finance.yahoo.com/lookup?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADWHxWef5zP0hg1AoYXQmoB6TRg0r0-ealt8bOCh26cWzJ9sqQQjgxKni-4Vw3nV5Qx00TEFwO64TRdAZ1VG_BmBN5a1KC-2RcFym1v81e1Wg1FpavrWkifT30ROV7_MToBet7ULCSCTKIc4WFFIBUbgnDlWJvwdrcu3BL5lgBbi
class HistoricalData:

    #protected data members
    _data= "";
    
    # constructor
    def __init__(self, ticker, period): 
        self._ticker = ticker
        self._period = period 
        
    def loadData(self):
        # "NVDA", '512d'
        self._data = yf.Ticker(self._ticker).history(period=self._period)
        # Show info
        
        
class Utils:

    def getCurrentTime():
        datetime.now().strftime('%H%M%S')

    def getCurrentDate():
        datetime.now().strftime('%Y%m%d')

    def getCurrentDatetime():
        return datetime.now().strftime('%Y%m%d%H%M%S')         
    

class DrawImage(HistoricalData):

    #protected data memebers
    _size = "";
    _img= "";
    
    # constructor
    def __init__(self, size, ticker): 
        self._size = size
        self._img = np.array(Image.new("RGB", (size,size)))
        HistoricalData.__init__(self, ticker, str(size)+"d") 
        self.loadData()
    
    def getValues(self):
        print("Ticker: ", self._ticker, "; Image Size: ", self._size);
        print(self._data.info())
        

    def draw(self):
        _dt = Utils.getCurrentDatetime()
        for r in range(0, self._size):
            for c in range(0, self._size):
                #print( data['Open'][r], data['Close'][c], data['High'][r] )
                re = self._data['Open'][r]
                gr = self._data['Close'][c]
                bl = self._data['High'][r]#365#data['Close'][r]
                self._img[r][c]=[re,gr,bl]
        img = Image.fromarray(self._img, 'RGB')
        
        img.save("textures/" + _dt + "_" + self._ticker + "_" + self._period + "OCH_color" + ".png") #OCH = Open Close High
        img = img.convert("L")
        img.show()
        img.save("textures/" + _dt + "_" + self._ticker + "_" + self._period + "OCH_bw" +".png");
        

obj = DrawImage(512, "ORCL") # NVDA, ABNB
obj.getValues()
obj.draw();