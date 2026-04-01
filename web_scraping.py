import pandas as pd
import requests
from bs4 import BeautifulSoup

# print(requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text)
# import requests

url = 'https://www.upwork.com/freelance-jobs/web-scraping/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
# soup = BeautifulSoup(response.content, 'lxml')

print(soup.prettify())
print(response.text)

# print(soup.find_all('h1')[0].text)