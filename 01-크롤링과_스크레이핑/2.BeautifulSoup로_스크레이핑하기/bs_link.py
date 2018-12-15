from bs4 import BeautifulSoup 

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com" title="go to naver">naver</a></li>
    <li><a href="http://www.daum.net" title="go to daum">daum</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

for a in links:
    href = a.attrs['href']
    title = a.attrs['title']
    text = a.string
    print(text, ">", title, ">", href, sep=',,,')
# 출력결과
# naver > go to naver > http://www.naver.com
# daum > go to daum > http://www.daum.net

# 출력 문자열들 사이에 공백이 생기는 이유는?
# 기본으로 sep=' '으로 설정. => print 맨 마지막에 sep=''추가

# 응용 sep=',,,'으로 설정시 
# naver,,,>,,,go to naver,,,>,,,http://www.naver.com 출력!