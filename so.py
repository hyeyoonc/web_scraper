import requests
from bs4 import BeautifulSoup

URL = f"http://stackoverflow.com/jobs?q=pyhon&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)
# 함수의 결과를 int(last_page)로 도출

def extract_job(html):
    title = html.find("h2", {"class": "mb4 fc-black-800 fs-body3"}).find("a")["title"]
    company, location = html.find("h3", {
        "class": "fc-black-700 fs-body1 mb4"
    }).find_all(
        "span", recursive=False)
        # list에 두개의 요소가 담겨있는 것을 알기때문에 분할 가능 
        #recur이거는: 가장 첫 단계의 span만 가져옴 
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html['data-jobid']
    return {
        'title': title,
        'company': company,
        'location': location,
        "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
    }
# last_page는 int가 되어야 range사용 가능
# .status_code는 연결 확인방법

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO:Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
          job = extract_job(result)
          jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
