from utils import generateValues

#Class stock calls function to generate the values
class Stock:
    def __init__(self):
        self.historic = generateValues()

    #Method price receives a date, if the date is not in the historic, returns -1
    def price(self, date):
        if date in self.historic:
            return self.historic[date]
        else:
            return -1
            