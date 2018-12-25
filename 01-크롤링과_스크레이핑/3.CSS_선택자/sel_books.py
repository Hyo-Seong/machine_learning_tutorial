from bs4 import BeautifulSoup
fp = open("./books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)
    
# 파이썬에서 람다는 멀티라인을 지원하지 않는다..
# 참고링크 : https://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not

sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("#bible #nu")
sel("#bible > #nu")
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")

print(soup.select("li")[3].string)