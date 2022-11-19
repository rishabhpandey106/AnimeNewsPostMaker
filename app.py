from flask import Flask,render_template
import requests
from bs4 import BeautifulSoup

# def extract():
#     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
#     url="https://otakumode.com/news"
#     r=requests.get(url,headers)
#     return r.status_code

# print(extract)

app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():

    url="https://otakumode.com/news"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    outerdata=soup.find_all("article",class_="p-article p-article-list__item c-hit p-article-list--sm",limit=6)
    # outerdata=soup.find_all("div",class_="p-article-list__body",limit=5)
    finalnews=""

    for data in outerdata:
        # news=soup.find("div",class_="p-article-list__body")
        news2=data.div.next_sibling.h3.a.string
        finalnews+= "\u2022 "+news2+ "\n"
    return render_template("index.html",News=finalnews)