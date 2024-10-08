#this code will take from the webscrapping file and add it to our csv
import csv
#import os
import trainingdatascrapper

# Function to fetch data from the web scraping script (assumed to return a list of scraped data)
def get_scraped_data(url):
    data = trainingdatascrapper.get_list_of_data(url)
    if data == []:
        return ["No returned data"]
    else:   
        return data

# Function to append data to a CSV file
def append_to_csv(filename, url):
    data = get_scraped_data(url)
    
   

    # Open file in write mode because we want this to either create a new file or we want it to overwrite an old file 
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        

        # Write the data rows
        
            
        for item in data:
            writer.writerow(item)
        


    
