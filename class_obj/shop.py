class Shop: # creating the class
    items=[]    # creating the empty item list
    prices=[]   # creating the empty price list
    stocks=[]   # creating the empty stock list
    
    def __init__(self): # creating the empty constructor 
        self.items=["tea","coffee","vadai"] # assigning items,prices and stocks to lists
        self.prices=[10,15,6]
        self.stocks=[50,50,30]
        
    def menuItems(self):    # menu function to show the menu 
        print("-----------------------------")
        print(f"Snakcs : {self.items}")
        print(f"Prices : {self.prices}")
        print(f"Stocks : {self.stocks}")
        print("-----------------------------\n")
    def buyItem(self,item,quantity,):   # buying snacks function
        self.item=item
        for index,product in enumerate(self.items):
            if product in item: # if my product is found then i'm subtracting the quantity to stock
                self.total_price=quantity*self.prices[index]    # number of quantity * price of the item is stored in price
                self.stocks[index]-=quantity
                print("-----------------------------")
                print(f"Ordered item is  : {self.item}")
                print(f"Quantity : {quantity}")
                print(f"Total Price : {self.total_price}")
                print("-----------------------------\n")
                break
            
    def show(self):
        print("-----------------------------")
        print(f"Available items : {self.items}")
        print(f"Prices : {self.prices}")
        print(f"Stocks : {self.stocks}")
        print("-----------------------------\n")
                
s = Shop()
s.menuItems()
s.buyItem("tea",5)
s.show()