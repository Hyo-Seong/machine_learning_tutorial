from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from selenium import webdriver


def getHtml(scrapingUrl):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('C:/Users/hyoseong/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=options)

    driver.get(scrapingUrl)
    html = driver.page_source
    return BeautifulSoup(html, 'html.parser')


def checkSizeList(scrapingUrl):
    soup = getHtml(scrapingUrl)
    list = soup.findAll('option')
    sizeList = []
    for i in range(2, len(list)):
        sizeList.append(list[i]['value'])
    return sizeList

def checkRestock(scrapingUrl, size):
    req = Request(scrapingUrl)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.select("#option > tr > td > select > option >text")[2])

if __name__ == "__main__":
    print("확인하려는 87MM의 링크를 입력하세요 >> ", end='')
    scrapingUrl = input()

    sizeList = checkSizeList(scrapingUrl)
    print("\n사이즈를 입력하세요 ")
    for idx, val in enumerate(sizeList):
        print(idx + 1, "\b.", val)
    print("번호를 입력하세요. >> ", end='')
    size = input()
    # checkRestock(scrapingUrl, size)   