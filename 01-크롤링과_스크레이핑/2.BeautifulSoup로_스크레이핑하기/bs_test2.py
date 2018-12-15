from bs4 import BeautifulSoup

html = """
<html><body>
  <h1 하이루="title">스크레이핑이란?</h1>
  <p id="body">웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(하이루="title")
# 작동한다. 꼭 html에 정의된 태그가 아니여도 방식이 같으면 작동하나보다.
body = soup.find(id="body")

print("#title=" + title.string)
print("#body=" + body.string)