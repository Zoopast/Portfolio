from utils import verifyAndTransformDates
from dateutil.relativedelta import relativedelta

class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def profit(self, date1: str, date2: str, annualized = False):
        startDate, endDate = verifyAndTransformDates(date1, date2)

        if annualized:
            startCapital = 0
            endCapital = 0
            for stock in self.stocks:
                startCapital += self.stocks[stock].price(startDate)
                endCapital += self.stocks[stock].price(endDate)
            revenue = (endCapital - startCapital) / startCapital
            dateDiff = relativedelta(endDate, startDate)
            finalAnnualizedRevenue = (((1 + revenue) ** (1 / dateDiff.years)) - 1)
            return round(finalAnnualizedRevenue, 2)
        else:
            profit = 0
            for stock in self.stocks:
                startValue = self.stocks[stock].price(startDate)
                endValue = self.stocks[stock].price(endDate)
                if startValue != -1 and endValue != -1:
                    profit += endValue - startValue
            
            return profit