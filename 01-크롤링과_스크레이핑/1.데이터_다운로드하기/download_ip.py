import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")

txtPath = 'download/download_ip_result.txt'

with open(txtPath, 'w', encoding='utf8') as f:
      f.write(text)
# 응용 파일에 저장하기
# 주의할점 : 기존 파일에 있던 데이터는 사라지고 새로 작성된다.
# 해결법 : 'w'를 'a' 로 바꿔준다.

# r(read), w(write), a(append)
# t(text) : 자동 인코딩/디코딩 모드
# b(binary) : 바이너리 모드
# 참고링크 : https://kimdoky.github.io/python/2017/11/28/python-file_object.html