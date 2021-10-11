from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://duunitori.fi/tyopaikat/?haku=python&alue=').text
soup = BeautifulSoup(html_text, 'lxml')
#jobs = soup.find_all('a',class_='job-box__hover gtm-search-result')
#first_job = jobs[0].text.replace(' ','') #first element without spaces
#print(first_job)
#for job in jobs:
  #  print(job.text)

#Get title and location of first job
#job = soup.find(class_='job-box__hover gtm-search-result')
#job_content = soup.find(class_='job-box__content')
#job_location = job_content.find(class_='job-box__job-location').text.replace('\n', '')

#print(f"{job.text} is available in {job_location}")

# get all jobs listed on a page
jobs = soup.find_all(class_='job-box__content')

for job in jobs:
    job_title = job.find(class_='job-box__title').text
    job_location = job.find('span',class_='job-box__job-location').text.split('-',1)[0].replace('\n','')
    print(f'{job_title} is available in {job_location}')

#ToDo remove "-" after Location and drop other text

