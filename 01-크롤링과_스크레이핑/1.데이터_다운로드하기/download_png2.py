import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "download/test2.png"

mem = urllib.request.urlopen(url).read()


with open(savename, mode = "wb") as f:
    f.write(mem)
    print('저장되었습니다...!')
# with 구문은 c#의 using 구문과 비슷한 것 같다.
# with 구문 참고링크 : https://soooprmx.com/archives/4079