from utils import verifyDates

class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def profit(self, date1, date2, annualized = False):
        startDate, endDate = verifyDates(date1, date2)
        if annualized:
            return self.getAnnualizedReturn(startDate, endDate)
        else:
            return self.calculateProfit(startDate, endDate)
    
    def getAnnualizedReturn(self, startDate, endDate):
            """
                Calculates and returns the 
                annualized return between 2 dates.
            """
            startCapital, endCapital = self.calculateCapitals(startDate, endDate)
            revenue = (endCapital - startCapital) / startCapital
            dateDiff = endDate.year - startDate.year
            ar = self.getAnnualizedReturnValue(revenue, dateDiff)
            
            return round(ar, 2) * 100

    def calculateCapitals(self, startDate, endDate):
            startCapital = 0
            endCapital = 0
            for stock in self.stocks:
                startCapital += self.stocks[stock].price(startDate)
                endCapital += self.stocks[stock].price(endDate)

            return startCapital, endCapital
    
    def calculateProfit(self, startDate, endDate):
            profit = 0
            for stock in self.stocks:
                startValue = self.stocks[stock].price(startDate)
                endValue = self.stocks[stock].price(endDate)
                if startValue != -1 and endValue != -1:
                    profit += endValue - startValue
            
            return profit
    
    def getAnnualizedReturnValue(self, revenue, dateDiff):
        if dateDiff == 0:
            return 0
        #Math magic
        return (((1 + revenue)**(1 / dateDiff)) - 1)

        