from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print(urljoin(base, "/hoge.html"))
print(urljoin(base, "http://otherExample.com/wiki"))
print(urljoin(base, "//anotherExample.org/test"))

# urljoin() 함수를 이용하면 
# <a> 태그의 href 속성에 지정돼 있는 경로를 절대 경로로 쉽게 변환할 수 있다.
# p.44 발췌