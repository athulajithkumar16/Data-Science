# Import the necessary libraries
from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from a webpage
url = 'https://oxylabs.io/blog/python-web-scraping'
response = requests.get(url)
html_content = response.text

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')  # You can also use 'html.parser'

# Find the HTML elements containing the text you want to extract
# For example, let's extract the text from all <p> tags
paragraphs = soup.find_all('p')

# Extract and print the text from each <p> tag
for p in paragraphs:
    text = p.get_text()
    print(text)