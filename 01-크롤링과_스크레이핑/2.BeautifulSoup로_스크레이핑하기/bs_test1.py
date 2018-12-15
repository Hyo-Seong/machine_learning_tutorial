from bs4 import BeautifulSoup

html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

# BeautifulSoup(string, parser종류)
# parser종류 : html.parser, lxml, lxml-xml, xml, html5lib 등등..
# 참고링크 : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

h1 = soup.html.body.h2
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 존재하지 않는 태그를 입력시 print할때 오류 발생 ex) 
# h2 = soup.html.body.h2
# print("h2 = " + h2.string)
# AttributeError: 'NoneType' object has no attribute 'string' 
# NoneType을 체크하려면 다음 코드를 사용하자.
# if variable is not None: ...
# 참고링크 : https://stackoverflow.com/questions/23086383/how-to-test-nonetype-in-python

print("h1 = " + h1.string)
print("p1 = " + p1.string)
print("p2 = " + p2.string)

# hi.string 대신 h1을 하면 => TypeError: Can't convert 'Tag' object to str implicitly 발생!