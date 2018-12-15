from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

# NoneType Check!
if soup.find("title") is not None:
    title = soup.find("title").string
if soup.find("wf") is not None:
    wf = soup.find("wf").string

print(title, end='')
print(wf)

# print하면 자동 줄바꿈을 해준다. 만약 줄바꿈을 원치 않는다면?
# print(text, end='')을 사용하자.