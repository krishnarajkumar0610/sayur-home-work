class Shop:
    items=[]
    prices=[]
    stocks=[]
    
    def __init__(self):
        self.items=["tea","coffee","vadai"]
        self.prices=[10,15,6]
        self.stocks=[50,50,30]
        
    def menuItems(self):
        print(f"Snakcs : {self.items}")
        print(f"Prices : {self.prices}")
        print(f"Stocks : {self.stocks}")

    def buyItem(self,item,quantity,s):
        for index,product in enumerate(self.items):
            if product in item:
                self.total_price=quantity*self.prices[index]
                self.stocks[index]-=quantity
                break
            
    def show(self):
        print(f"Available items : {self.items}")
        print(f"Prices : {self.prices}")
        print(f"Stocks : {self.stocks}")
                
s = Shop()
s.menuItems()
s.buyItem("tea",5,s)
s.show()