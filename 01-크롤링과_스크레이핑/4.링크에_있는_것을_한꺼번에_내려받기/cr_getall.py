from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

proc_files = {}

URL = "https://docs.python.org/3.5/library/"

def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    # a 태그에 href속성이 있는 태그들을 모음.

    result = []

    for a in links:
        href = a.attrs['href']
        # 그 중 href속성안의 값을 꺼냄
        url = urljoin(base, href)
        # 경로를 절대경로로 변환한 뒤,
        result.append(url)
        # result 배열에 url 추가
    return result

def download_file(url):
    o = urlparse(url)
    # o value : ParseResult(scheme='https', netloc='docs.python.org', path='/3.5/_static/pydoctheme.css', params='', query='', fragment='')
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):
    # 만약 경로중에 ..../ 로 끝나는게 있으면 index.html 추가해줌
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    # dirname(filepath) 은 뒤에 파일명을 빼준다. (파일이 속한 폴더경로를 반환한다.)

    if os.path.exists(savepath): return savepath
    # 이미 존재한다면 다운로드 과정 뛰어넘음.

    if not os.path.exists(savedir):
    # 파일을 다운해야 할 경로가 존재하지 않는다면
        print("mkdir : ", savedir)
        makedirs(savedir)
        # 폴더 만들기
    try:
        print("download : ", url)
        urlretrieve(url, savepath)
        # 파일을 해당 경로에 다운.
        time.sleep(1) # 1초이다 | 1ms 아님!
        # 너무 빠르면 서버에서 락을 거나?
        # 네트워크가 안좋으면 못버티고 오류를 반환하나?

        return savepath
    except:
        print("download fail : ", url)
        return None

def analyze_html(url, root_url):
    savepath = download_file(url)
    
    if savepath is None: return
    # 경로가 잘못되었거나 경로에 파일이 존재하지 않을 때 (404)

    if savepath in proc_files: return
    # 이미 다운로드한 파일일 경우
    # 이 부분은 다운로드 하기전에 거를 순 없을까..

    proc_files[savepath] = True
    # 저장된 것이라는 표식을 남김

    print("analyze_html : ", url)

    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)

    for link_url in links:
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue
            # css파일에는 a href가 없기 때문에.
        if not re.search(r".(html|htm)$", link_url):
        # 다운하려는 파일이 html 이나 htm이면 태그 분석(재귀)
            analyze_html(link_url, root_url)
            continue
        download_file(link_url)
        # 밑에까지 쭉 내려갔다가 올라와서 자기자신 다운로드하고 한단계 위로 올라감. (피보나치와 비슷)

if __name__ == "__main__":
    url = URL
    # url 설정은 맨 위에서 하자.

    analyze_html(url, url)
    # 첫 호출만 하면 main의 역할은 끝난다 재귀는 analyze_html 에서 수행한다.