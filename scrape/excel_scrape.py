import requests, re 
from bs4 import BeautifulSoup

url = 'https://www.udemy.com/course/microsoft-excel-2013-from-beginner-to-advanced-and-beyond/'

response = requests.get(url)
# print(response)
html_content = response.text
# print(html_content)

soup = BeautifulSoup(html_content, 'lxml')
span = soup.find_all('span', {'class': 'section--section-title--svpHP'} )
# blog_titles = soup.find_all('a', class_=re.compile('oxy-rmqaiq'))
# print(span)


for i in span:
    text = i.get_text()
    print(text)

# <span class="truncate-with-tooltip--ellipsis--YJw4N " style="-webkit-line-clamp: 2;">Section 2: Microsoft Excel Fundamentals</span>
# <span class="truncate-with-tooltip--ellipsis--YJw4N " style="-webkit-line-clamp: 2;">Section 3: Entering and Editing Text and Formulas</span>

#
