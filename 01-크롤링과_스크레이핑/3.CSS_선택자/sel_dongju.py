from bs4 import BeautifulSoup
import urllib.request as req

# https://ko.wikisource.org/wiki/저자:윤동주 <= 로 실행하면 ??
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128) ERROR!!

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

# a_list = soup.select("#mw-content-text > div > li a")
# 이 책이 나온 뒤 위키의 HTML구조가 바뀌어서 기존 코드로는 동작을 안한다.

a_list = soup.select("#mw-content-text > div > ul > li a")
for a in a_list:
    name = a.string
    print("-", name)