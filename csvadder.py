#this code will take from the webscrapping file and add it to our csv
import csv
import os
import MFwebscrapper

# Function to fetch data from the web scraping script (assumed to return a list of scraped data)
def get_scraped_data():
    # Simulating reading data from the webscraping script
    # You can replace this with an actual call to your scraping function or import the necessary function
    data = MFwebscrapper.get_content()
    return data

# Function to append data to a CSV file
def append_to_csv(data, filename="scraped_data.csv"):
    file_exists = os.path.isfile(filename)

    # Open file in append mode
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header only if the file does not exist
        if not file_exists:
            writer.writerow(["Headline"])  # Modify the header based on the structure of your data

        # Write the data rows
        for item in data:
            writer.writerow([item])

def main():
    # Get the scraped data
    scraped_data = get_scraped_data()

    # Append it to the CSV file
    append_to_csv(scraped_data)

if __name__ == "__main__":
    main()
