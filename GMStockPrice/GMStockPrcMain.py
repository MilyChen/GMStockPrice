'''
Created on Sep 4, 2020

@author: Mily
'''
from selenium import webdriver
import pandas as pd
import datetime
from selenium.webdriver.firefox.options import Options


tdate = datetime.datetime.now()
today = tdate.strftime("%w")

#today = 2
if today > 1   : # run on weekdays only, 0 = sunday  script runs at 3am for previous day... 
    lastprices = []
    highprice = []
    lowprice = []
    pdates = []
    tickers = [ 'XIC-T', 'QTIP-NE', 'XEF-T', "ZFL-T", "ZAG-T","EEMV-A", "ACWV-A", "VTI-A"]
    website = "https://www.theglobeandmail.com/investing/markets/stocks/"
    
    options = Options()
    options.add_argument('--headless')
    
    firefoxdriver = "C:\Users\Mily.mc-pc\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe"
    driver = webdriver.Firefox( firefox_options=options,executable_path=firefoxdriver)
    
    
    for ticker in tickers:
        url = website + ticker
        driver.get(url) #this will refresh the page..
        
        try:
            #inspect page element, in the code copy selector
            price = driver.find_element_by_css_selector("span.quote-detail-info-field.lastPrice-value > span.barchart-overview-field-value").text
            #pdate = driver.find_element_by_css_selector("span.quote-detail-info-field.tradeTime-value").text #stocks last update date
            pdate = (tdate+ datetime.timedelta(days=-1)).strftime("%x")
            
            low= driver.find_element_by_css_selector("span.lowPrice.price-field").text
            high = driver.find_element_by_css_selector("span.highPrice.price-field").text
        except: #ticker doesn't exist
            price ="n/a"
            pdate = "n/a"
            low = "n/a"
            high = "n/a"
      
        lowprice.append(low)
        highprice.append(high)
        lastprices.append(price)
        pdates.append(pdate)
        print (price)
    
    driver.quit()
    df = pd.DataFrame({'PriceDate':pdates,'StockNames':tickers,'LastPrice':lastprices,'High':highprice,'Low':lowprice}) 
    
    savepath = 'C:\\Users\\Mily.mc-pc\\eclipse\\ws_portfolio_tracker\\'
    
    df.to_csv(savepath + 'ws2.csv', index=False, encoding='utf-8', header=False, mode='a') # new file
print ("Finished ;)")