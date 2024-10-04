import MFwebscrapper
import MFstockdata
import csvadder



def training_data():
    #this is going to scrape data that will serve as baseline(training data for the model)
    SMP500 = MFstockdata.Stock("^GSPC")
    url = SMP500.get_url()
    csvadder.append_to_csv("modelT_data", url)
    