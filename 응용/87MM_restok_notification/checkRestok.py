from bs4 import BeautifulSoup


def checkRestock(scrapingUrl):
    print(scrapingUrl)

if __name__ == "__main__":
    print("확인하려는 87MM의 링크를 입력하세요 >> ", end='')
    scrapingUrl = input()

    checkRestock(scrapingUrl)
