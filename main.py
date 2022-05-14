from portfolio import Portfolio
from stock import Stock
from utils import stocksForPorfolio


if __name__ == "__main__":
    date1, date2 = "14/05/2020", "14/05/2022"
    chosenStocks = stocksForPorfolio()
    stocks = {}

    for stock in chosenStocks:
        stocks[stock] = Stock()

    portfolio = Portfolio(stocks)

    #Profit from portfolio
    profit = portfolio.profit(date1, date2)
    print(f"Profit from portfolio: ${profit}")
    #Annualized return from portfolio
    profit = portfolio.profit(date1, date2, annualized = True)
    print(f"Annualized return from portfolio: {profit}")