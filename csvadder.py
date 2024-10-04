#this code will take from the webscrapping file and add it to our csv
import csv
#import os
import MFwebscrapper

# Function to fetch data from the web scraping script (assumed to return a list of scraped data)
def get_scraped_data():
    data = MFwebscrapper.get_content()
    if data == []:
        return ["No returned data"]
    else:   
        return data

# Function to append data to a CSV file
def append_to_csv(filename):
    data = get_scraped_data()
    
   

    # Open file in write mode because we want this to either create a new file or we want it to overwrite an old file 
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        

        # Write the data rows
        for item in data:
            writer.writerow([item])

def run_adder_on_file(filename): # this is basically a getter function to be called in MF analysis
    append_to_csv(filename)
    
