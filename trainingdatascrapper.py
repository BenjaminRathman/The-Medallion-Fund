
import requests
from bs4 import BeautifulSoup

# Function to get the HTML content from a URL with a User-Agent header
def get_html_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

# Function to parse the HTML content using BeautifulSoup and extract table data
def extract_table_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table (inspect the page to confirm the right table class or tag)
    table = soup.find('table')  # Find the first table; adjust this if multiple tables exist
    if not table:
        print("Table not found.")
        return []

    # Extract table rows (<tr>)
    rows = table.find_all('tr')

    # Extract table headers (<th>) to get column names
    headers = [th.get_text().strip() for th in rows[0].find_all('th')]

    # Extract the data from each row (<td>)
    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.get_text().strip() for col in cols]
        data.append(cols)

    return headers, data

# Main function to scrape data from the given URL and store in a list
def scrape_data(url):
    html_content = get_html_content(url)
    if html_content:
        headers, data = extract_table_data(html_content)
        if data:
            # Combine headers and data into a single list
            result = [headers] + data
            return result
        else:
            print("No data extracted.")
            return None
    else:
        return None


# Display the extracted data
def get_list_of_data(url):
    return scrape_data(url)
