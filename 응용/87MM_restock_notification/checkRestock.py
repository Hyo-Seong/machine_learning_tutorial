from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def checkRestock(scrapingUrl):
    req = Request(scrapingUrl)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.select("#option > tr > td > select > option")[2].string)

if __name__ == "__main__":
    print("확인하려는 87MM의 링크를 입력하세요 >> ", end='')
    scrapingUrl = input()

    print("\n사이즈를 입력하세요(S,M,L) >> ", end='')
    scrapingUrl = input()
    checkRestock(scrapingUrl)