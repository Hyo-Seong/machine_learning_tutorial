from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def getHtml(scrapingUrl):
    req = Request(scrapingUrl)
    html = urlopen(req).read()
    return BeautifulSoup(html, 'html.parser')

def checkSizeList(scrapingUrl):
    soup = getHtml(scrapingUrl)
    list = soup.findAll('option')
    for l in list:
        print(l.string)

def checkRestock(scrapingUrl, size):
    req = Request(scrapingUrl)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.select("#option > tr > td > select > option >text")[2])

if __name__ == "__main__":
    print("확인하려는 87MM의 링크를 입력하세요 >> ", end='')
    scrapingUrl = input()

    checkSizeList(scrapingUrl)
    # print("\n사이즈를 입력하세요(S,M,L) >> ", end='')
    # size = input()
    # checkRestock(scrapingUrl)