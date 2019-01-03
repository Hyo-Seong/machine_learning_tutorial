87MM 재입고 알람 서비스입니다.

제작동기 : 87MM 재입고 알람 SMS를 신청했는데 제대로 작동을 하지 않아서 제작하게 되었습니다.

==========

개발도중 발생한 문제

품절 여부를 스크레이핑하던 도중 html코드가 javascript로 동적으로 받아와 BeautifulSoup로는 파싱이 불가함.

그러던 도중
https://www.facebook.com/groups/codingeverybody/permalink/2602214939819026/

나와 비슷한 문제가 발생한 사람을 발견했고, 여기서 해결책을 찾으려 하였다.

댓글속 참고링크 : 
https://www.slideshare.net/wangwonLee/2018-datayanolja-moreeffectivewebcrawling?fbclid=IwAR0q6Hz0Oxaxu1NjYJu29wOcl1_ZkLVciuKDxN4OTeV1tvGcNxwU8QipIhE

우선 웹드라이버를 사용해보기로 하였다.
참고링크 : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/