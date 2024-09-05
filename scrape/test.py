import requests
from bs4 import BeautifulSoup

url = 'https://oxylabs.io/blog'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

import re
# Send a request and pass the response to Beautiful Soup just like before

blog_titles = soup.find_all('a', class_=re.compile('oxy-rmqaiq'))
for title in blog_titles:
    print(title.text)