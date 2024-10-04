#here is where we can gather information on a stock 
import csvadder

class Stock:
    def __init__(self, actual_marketcap, num_of_shares, share_price, tkr_symbl):
        self.actual_marketcap = actual_marketcap 
        self.data = []
        self.num_of_shares = num_of_shares
        self.models_marketcap = 0
        self.models_shareprice = 0
        self.share_price = share_price
        self.tkr_symbl = tkr_symbl
        self.url = ""

    def update_data(self, filename):
        self.data = csvadder.run_adder_on_file(filename) # this should update the file that contains the data we want 
    
    
    def get_models_shareprice(self):
        self.models_shareprice = (self.models_marketcap/self.num_of_shares)
        
    def get_url(self):
        base_url = "https://finance.yahoo.com/quote/"
    
    # Construct the full URL
        self.url =  f"{base_url}{self.tkr_symbl}"
    
        