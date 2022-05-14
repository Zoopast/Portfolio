
import datetime
import random

from data import FAANG, DAYS_TO_TEST, STOCK_MAX_VALUE

#Transform the two dates into a datetime variable,
#After that, checks if the first date is after the second date, if so, swap them
def verifyAndTransformDates(d1: str, d2: str):
    startDMY = d1.split("/")
    endDMY = d2.split("/")
    start = datetime.date(day=int(startDMY[0]), month=int(startDMY[1]), year=int(startDMY[2]))
    end = datetime.date(day = int(endDMY[0]), month = int(endDMY[1]), year = int(endDMY[2]))

        #if start date is after end date, swap them
    if start > end:
        start, end = end, start
        
    return start, end

#Choose a random amount of companies to be part of the portfolio
def stocksForPorfolio():
    qtyOfStocks = random.randint(1, len(FAANG))
    portfolioStocks = []
    for i in range(qtyOfStocks):
        portfolioStocks.append(FAANG[i])

    return portfolioStocks   

#Generate values for a stock for the amount of days it will be tested
def generateValues():
    dates = {}

    for i in range(DAYS_TO_TEST, -1, -1):
        date = datetime.datetime.now().date() - datetime.timedelta(days=i)
        dates[date] = random.randint(0, STOCK_MAX_VALUE)
    return dates

    

