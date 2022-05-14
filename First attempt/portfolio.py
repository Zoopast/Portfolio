import json
import datetime


class Stock:
    def __init__(self, company, companyOwner, currentValue):
        self.companyOwner = companyOwner
        self.company = company
        self.currentValue = currentValue
        self.log = {}

    def price(self, date):
        if date in self.log:
            return self.log[date].copy().pop()
        else:
            return -1

    def getCurrentValue(self):
        return self.currentPrice
    
    def setCurrentValue(self, value):
        self.currentValue = value

    def addLog(self, stockDate, stockTime, stockValue):
        if stockDate in self.log:
            self.log[stockDate].append((stockTime, stockValue))
        else:
            self.log[stockDate] = [(stockTime, stockValue)]

        self.currentValue = stockValue
        

class Portfolio:
    
    def __init__(self, stocks = {}, companies = {}):
        self.stocks = stocks
        self.companies = companies

    def getStartAndEndDate(self, d1: str, d2: str):
        startDMY = d1.split("/")
        endDMY = d2.split("/")
        start = datetime.date(day=int(startDMY[0]), month=int(startDMY[1]), year=int(startDMY[2]))
        end = datetime.date(day = int(endDMY[0]), month = int(endDMY[1]), year = int(endDMY[2]))

        #if start date is after end date, swap them
        if start > end:
            d1, d2 = d2, d1
        
        return d1, d2


    def profit(self, d1:str, d2:str) -> float:
        d1, d2 = self.getStartAndEndDate(d1, d2)
        stockProfits = []
        s1 = 0
        s2 = 0

        for stock in self.stocks:
            st = self.stocks[stock][2]
            log = self.companies[stock].log

            if d1 in st and d2 in log:
                if st in log:
                    s1 = self.companies[stock].price(st)
                    s2 = self.companies[stock].price(d2)

                    stockProfits.append((s2[1] - s1[1]) * self.stocks[stock][1])
            else:
                print("Dates not valid")
        return round(sum(stockProfits), 2)
                

def loadData():
    companiesJS = json.load(open("companies.json", "r"))
    companies = {}

    for company in companiesJS["companies"]:
        companies[company["companyName"]] = Stock(company["companyName"], company["companyOwner"], company["currentValue"])

    stocksJS = json.load(open("stocks.json", "r"))

    for stock in stocksJS["stocks"]:
        companies[stock["company"]].addLog(stock["date"], stock["time"], stock["price"])


    portfolioJS = json.load(open("portfolio.json", "r"))
    portfolioStocks = {}
    
    for stock in portfolioJS["portfolio"]:
        portfolioStocks[stock["stockName"]] = [stock["stockName"], stock["qty"], stock["boughtDate"], stock["boughtTime"]]


    portfolio = Portfolio(portfolioStocks, companies)

    return portfolio


portfolio = loadData()
d1 = "15/04/2022"
d2 = "20/04/2021"
result = portfolio.profit(d1, d2)

print(f"The profit from portfolio between {d1} and {d2} is: {result}")

