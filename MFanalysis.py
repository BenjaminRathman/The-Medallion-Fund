#this is where we will do the analysis of the stock
from sklearn.model_selection import train_test_split # type: ignore
import pandas as pd # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore
import csvadder


class Stock:
    def __init__(self, actual_marketcap, num_of_shares, share_price):
        # Initialize the Stock object with marketcap and data
        self.actual_marketcap = actual_marketcap 
        self.data = []
        self.num_of_shares = num_of_shares
        self.models_marketcap = 0
        self.models_shareprice = 0
        self.share_price = share_price

    def update_data(self, filename):
        self.data = csvadder.run_adder_on_file(filename) # this should update the file that contains the data we want 
    
    
    def get_models_shareprice(self):
        self.models_shareprice = (self.models_marketcap/self.num_of_shares)