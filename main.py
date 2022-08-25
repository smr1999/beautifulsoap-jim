import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':

    keyword = 'python'

    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}&txtLocation=').text

    soup = BeautifulSoup(html_text,'lxml')

    total_posts = int(soup.find('span',id='totolResultCountsId').text.strip())

    per_page = 25
    
    # total_pages = total_posts//per_page+1
    total_pages =5

    jobs = []

    for i in range(1,total_pages+1):
        html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords={keyword}&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize={str(per_page)}&postWeek=60&txtKeywords=python&pDate=I&sequence={str(i)}&startPage={str((i%10)*10+1)}').text
        
        soup = BeautifulSoup(html_text,'lxml')
        jobs_ = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

        for job in jobs_:
            published_date = job.find('span',class_='sim-posted').span.text.strip()
            if 'Posted few days ago' in published_date:
                company_name = job.find('h3',class_='joblist-comp-name').text.strip()

                skills = job.find('span',class_='srp-skills').text.split(' , ')
                skills = [skill.strip() for skill in skills]

                published_date = job.find('span',class_='sim-posted').span.text.strip()

                jobs.append((company_name,skills))
        print(f'page {i}')
    
    print(jobs)