
import MFstockdata
import csvadder



def training_data(): #could probably implement a loop here 
    #this is going to scrape data that will serve as baseline(training data for the model)
    SMP500 = MFstockdata.Stock("CX")
    url = SMP500.get_url()
    csvadder.append_to_csv("modelT_data.csv", url)
    
    
training_data()

def gather_lst_data(url):
    csvadder.append_to_csv("modelT_data.csv", url)
    
gather_lst_data("https://www.macrotrends.net/stocks/charts/AAPL/apple/pe-ratio")