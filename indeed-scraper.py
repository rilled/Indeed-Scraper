from bs4 import BeautifulSoup
import requests

jobdb = []

for iterations in range(0,15,10):
    position, loc = 'Developer', 'Remote'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}
    url = requests.get('https://ca.indeed.com/jobs?q={0}&l={1}'.format(position, loc), headers)
    soup = BeautifulSoup(url.text, 'lxml')

    # Entry to page, getting to the layer in the table required for scraping
    for entry in soup.find_all('div', {'class': 'job_seen_beacon'}):
        t1 = entry.find('tbody')
        t2 = t1.find('tr')

        # Scrape Job Title
        for name in t2.find_all('h2',{'class':'jobTitle jobTitle-color-purple jobTitle-newJob'}):
            title = name.find_all('span')[1].get_text()

            # Scrape Company Name
            company_div = t2.find('div',{'class':'heading6 company_location tapItem-gutter companyInfo'})
            company_span = company_div.find('span')
            company = (company_span.get_text())

            # Scrape Salary
            if t2.find('div',{'class':'salary-snippet'}):
                salary = t2.find('div',{'class':'metadata salary-snippet-container'}).get_text()
            else:
                salary = "No Salary Listed"

            # Scrape Location
            if t2.find('div',{'class':'companyLocation'}):
                location = t2.find('div',{'class':'companyLocation'}).get_text()
            else:
                location = "No Location Listed"

            jobdb.append([title, company, salary, location])
print(jobdb)
