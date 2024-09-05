from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up options for Brave
brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"  # Replace with the actual path to Brave's executable
options = Options()
options.binary_location = brave_path

# Set up Selenium to use Brave browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Open the Udemy course page
url = 'https://www.udemy.com/course/microsoft-excel-2013-from-beginner-to-advanced-and-beyond/'
driver.get(url)

# Allow time for the page to fully load
driver.implicitly_wait(10)

# Use BeautifulSoup to parse the loaded page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all the course content headings
headings = soup.find_all('span', class_='section--section-title--8blTh')

# Print the extracted headings
for heading in headings:
    print(heading.text)

# Close the browser
driver.quit()
