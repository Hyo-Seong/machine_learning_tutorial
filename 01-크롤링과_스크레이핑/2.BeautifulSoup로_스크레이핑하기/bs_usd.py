from bs4 import BeautifulSoup
import urllib.request as req

url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value").string
print("usd/krw = " + price)

# 책에는 결과가 1,147,50 => 오탈자 찾았다
# 지금은 결과가 1,134.50
# 달러좀 사야되나?