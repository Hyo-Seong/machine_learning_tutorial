import sys
import urllib.request as req
import urllib.parse as parse
# 여기서 as는 alias(별칭)을 뜻함.

if len(sys.argv) <= 1:
    print("USAGE: download_forecast_argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : regionNumber
}

params = parse.urlencode(values)

url = API + "?" + params

data = req.urlopen(url).read()
text = data.decode("utf-8")

txtPath = "download/download_forecast_argv_result.txt"

with open(txtPath, 'w', encoding='utf8') as f:
      f.write(text)
# 실행방법 : python path/download_forecast_argv.py 108  <= sys.argv[1]
# sys.argv[0] => path/download_forecast_argv.py
# sys.argv[2] => IndexError: list index out of range

# ex) python  download_forecast_argv.py 108 102
# sys.argv[2] => 102