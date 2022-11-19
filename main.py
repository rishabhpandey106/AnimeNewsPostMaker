import requests
from bs4 import BeautifulSoup

def extract():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url="https://www.livechart.me/anime/10257"
    r=requests.get(url,headers)
    return r.status_code

print(extract)