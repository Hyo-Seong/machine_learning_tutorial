from urllib.parse import urljoin

base = "http://example.com/html/aa.html"

# urljoin은 상대경로를 절대경로로 변환한다.
# 만약 존재할 수 없는 경로를 입력한다면? 
# ex) ../../../../index.html
# 결과값 : http://example.com/index.html
# 더이상 위로 올라갈 게 없으면 최상위 경로로 지정한다.

print(urljoin(base, "b.html"))
print(urljoin(base, "sub/c.html"))
print(urljoin(base, "../../../../index.html"))
print(urljoin(base, "../img/hoge.png"))
print(urljoin(base, "../css/hoge.css"))