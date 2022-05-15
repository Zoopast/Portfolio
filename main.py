from portfolio import Portfolio
from stock import Stock
from utils import stocksForPorfolio, getDates

if __name__ == "__main__":
    date1, date2 = getDates()
    chosenStocks = stocksForPorfolio()
    stocks = {}

    for stock in chosenStocks:
        stocks[stock] = Stock()

    portfolio = Portfolio(stocks)

    #Profit from portfolio
    profit = portfolio.profit(date1, date2)
    print(f"Profit from portfolio: ${profit}")
    #Annualized return from portfolio
    ar = portfolio.profit(date1, date2, annualized = True)
    print(f"Annualized return from portfolio: {ar} or {ar}%")