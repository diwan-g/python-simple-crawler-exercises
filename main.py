from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://duunitori.fi/tyopaikat/?haku=python&alue=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('a',class_='job-box__hover gtm-search-result')


for job in jobs:
    print(job.text)

