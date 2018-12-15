import urllib.request
import urllib.parse
# API 정보 : http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId' : '108'
}

# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
# 참고링크 : https://docs.python.org/3/library/urllib.parse.html
# 사실 완벽히 이해하지는 못했다.
params = urllib.parse.urlencode(values)

# GET 방식
url = API + "?" + params

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')

txtPath = "download/download_forecast_result.txt"

with open(txtPath, 'w', encoding='utf8') as f:
      f.write(text)
# f.write(data) => TypeError: write() argument must be str, not bytes 라는 오류를 반환 
# decode 후 encode 하자.
