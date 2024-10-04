#this is the webscrapping script 
#going to take from yahoo finance 
import MFstockdata

import requests # type: ignore
from bs4 import BeautifulSoup  # type: ignore

# Function to get the HTML content from a URL
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

# Function to parse the HTML content using BeautifulSoup
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

# Function to extract specific data (example: headlines from a news site)
def extract_data(soup):
    data = []
    # Modify the below example based on the structure of the website
    for item in soup.find_all('h2'):  # Example: finding all headlines in <h2> tags
        headline = item.get_text().strip()
        data.append(headline)
    
    return data

# Main function to scrape a website
def get_content():
    url = "https://example.com"  # Replace with the website you want to scrape
    html_content = get_html_content(url)
    
    if html_content:
        soup = parse_html(html_content)
        data = extract_data(soup)
        
        # Output the scraped data
        
        rlist = []
        for item in data:
            rlist += [item]
        return rlist
        
        
#if __name__ == "__main__":
 #   get_content()
