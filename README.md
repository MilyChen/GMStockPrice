# GMStockPrice

Scrapes Globe&Mail's website to grab the latest stock prices specified. Combined with Window's task scheduler to run daily, prices are automatically updated for you! The code is set to run only on weekdays as stock markets are closed weekends. 

Sample Stock: https://www.theglobeandmail.com/investing/markets/stocks/ENB-T/


## Python Libraries Needed
Selenium for scraping
Pandas for dataframes, exporting/saving the output


## Windows Task Scheduler Bat File (Sorry MacBook users, you'll need to look up Chron, Task Automater steps separately)
1. Open a notepad file
2. Type in the following: 
@echo off
"C:\Users\your computer path\python.exe" "C:\Users\your computer path\your python program.py"
3. Save the file ending in ".bat" to create a Windows Batch File
4. Open windows task scheduler, and create a new task that runs your bat file a certain time everyday.
