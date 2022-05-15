import datetime
import random
from data import FAANG, DAYS_TO_TEST, STOCK_MAX_VALUE

#Checks if the first date is after the second date, if so, swap them
def verifyDates(d1, d2):
    if d1 > d2:
        d1, d2 = d2, d1
    return d1, d2

#Choose a random amount of companies to be part of the portfolio
def stocksForPorfolio():
    qtyOfStocks = random.randint(1, len(FAANG))
    portfolioStocks = FAANG[:qtyOfStocks]

    return portfolioStocks   

#Generate values for a stock for the amount of days it will be tested
def generateValues():
    dates = {}

    for i in range(DAYS_TO_TEST, -1, -1):
        date = datetime.datetime.now().date() - datetime.timedelta(days=i)
        dates[date] = random.randint(0, STOCK_MAX_VALUE)
    return dates

def getDates():
    date1 = datetime.datetime.now().date()
    date2 = date1 - datetime.timedelta(days=DAYS_TO_TEST)
    return date1, date2

