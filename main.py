from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://duunitori.fi/tyopaikat/?haku=python&alue=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('a',class_='job-box__hover gtm-search-result')
first_job = jobs[0].text.replace(' ','')
print(first_job)


for job in jobs:
    print(job.text)

