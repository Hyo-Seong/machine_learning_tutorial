from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from selenium import webdriver
import os
    
def cls(): 
    os.system('CLS')


def initWebDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    # 설정한 옵션을 웹드라이버에 적용한다.
    global driver
    driver = webdriver.Chrome('C:/Users/hyoseong/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=options)
    cls()

def getHtml(scrapingUrl):
    driver.get(scrapingUrl)
    # 전체 페이지 코드를 불러온다. 코드를 가지고 있다가 가공은 다른 곳에서 진행된다.
    html = driver.page_source
    return BeautifulSoup(html, 'html.parser')


def checkSizeList(scrapingUrl):
    soup = getHtml(scrapingUrl)
    list = soup.findAll('option') # TODO - HyoSeong 이부분 수정해야함. option으로 찾으면 다른값 섞일수 있음.
    
    sizeList = []
    
    for i in range(2, len(list)):
        sizeList.append(list[i]['value'])
    
    if len(sizeList) == 0:
        print('사이즈정보를 받아들이지 못하였습니다.')
        getLink()

    chooseSize(sizeList)

def aaa(sizeList):
    print('aa')

def getLink():
    print("확인하려는 87MM의 링크를 입력하세요 >> ", end='')
    scrapingUrl = input()

    checkSizeList(scrapingUrl)

def checkRestock(scrapingUrl, size):
    req = Request(scrapingUrl)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.select("#option > tr > td > select > option >text")[2])

def chooseSize(sizeList):
    for idx, val in enumerate(sizeList):
        print(idx + 1, "\b.", val)
    print("원하는 사이즈의 번호를 입력하세요. >> ", end='')
    size = input()

    if not (int(size) <= len(sizeList) and int(size) > 0):
        cls()
        chooseSize(sizeList)


if __name__ == "__main__":
    initWebDriver()

    getLink()

    
    # checkRestock(scrapingUrl, size)