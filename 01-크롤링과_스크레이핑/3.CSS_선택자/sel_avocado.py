from bs4 import BeautifulSoup
fp = open("fruits_vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print(soup.select_one("li:nth-of-type(8)").string)
# li태그들을 다 모아 배열을 만든 후 8번째 요소를 출력

print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
# id가 ve-list인 것 들중에 li 중에 4번째

print(soup.select("#ve-list > li[data-lo='us']")[1].string)
# id가 ve-list인 것 들중에 data-lo가 us인 li의 배열을 만듦. 그중에 첫번째 요소 출력 
# 첫번째 print 와는 조금 다른 개념

print(soup.select("#ve-list > li.black")[1].string)
# id가 ve-list인  li중에 class가 black인 배열을 만듦. 그중에 첫번째 요소 출력

cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)
# tag : li, data-lo : us, class : black

print(soup.find(id="ve-list").find("li", cond).string)
# id : ve-list, tag : li, data-lo : us, class : black 