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

    dictHeaders = dict(O='Open', C='Close', H='High', L='Low', V='Volume', D='Dividends', S='Stock Splits')     
    

class DrawImage(HistoricalData):

    #protected data memebers
    _imgSize = "";
    _img= "";
    
    # constructor
    def __init__(self, size, ticker): 
        self._imgSize = int(size/2)
        
        HistoricalData.__init__(self, ticker, str(size)+"d") 
        self.loadData()
    
    def getValues(self):
        print("Ticker: ", self._ticker, "; Data period: " , self._period, "d", "; Image Size: ", self._imgSize);
        print(self._data.info())
        

    def draw(self, red, green, blue, alpha, rgba):
        _dt = Utils.getCurrentDatetime()
        if(rgba): 
            _prefix = "RGBA"
            self._img = np.array(Image.new("RGBA", (self._imgSize,self._imgSize)))
        else: 
            _prefix="RGB"
            self._img = np.array(Image.new("RGB", (self._imgSize,self._imgSize)))
        for r in range(0, self._imgSize):
            for c in range(0, self._imgSize):
                #print( data['Open'][r], data['Open'][c],data['Close'][c], data['High'][r] )
                #print( self._data['Open'][r], "-", self._data['Open'][c])
                re = self._data[red][r+c]
                gr = self._data[green][r+c]
                bl = self._data[blue][r+c]#365#data['Close'][r]
                if(rgba):
                    a = self._data[alpha][r+c]#365#data['Close'][r]
                    self._img[r][c]=[re,gr,bl, a]
                else:
                    self._img[r][c]=[re,gr,bl]
        if(rgba):
            img = Image.fromarray(self._img, 'RGBA')
        else:
             img = Image.fromarray(self._img, 'RGB')
        
        img.save("textures/" +  self._ticker + "_" + self._period + "OCH_color_" + _prefix + "_" + _dt + ".png") #OCH = Open Close High
        img = img.convert("L")
        img.show()
        img.save("textures/" + self._ticker + "_" + self._period + "OCH_bw_"  + _prefix + "_" + _dt +".png");
        
print(Utils.dictHeaders)
obj = DrawImage(512, "ORCL") # NVDA, ABNB
obj.getValues()
#obj.draw(red='Open', green='Close', blue='High', alpha='Low', rgba=True);
obj.draw(red='Open', green='Close', blue='High', alpha= '', rgba=False);