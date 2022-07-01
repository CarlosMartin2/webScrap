import requests
from bs4 import BeautifulSoup
baseUrl = 'https://www.volunteerconnector.org'
single_page = requests.get(baseUrl)
soup = BeautifulSoup(single_page.content, 'html.parser')

all_links =  soup.select('a')

for page in all_links:
    linkTo = page.get('href')
    page_content = requests.get(linkTo)
    soup_each = BeautifulSoup(page_content.content, 'html.parser')
    print(linkTo)