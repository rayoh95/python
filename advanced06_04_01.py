# Asyncio
# 비동기 I/O Coroutine 작업(동기는 기다려야 한다. 비동기는 기다리지 않고 바로 실행. 다음 제어권을 넘겨 다음 워커가 일할 수 있게 해준다.)
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점 부터 재실행하는 원리
# Non-Blocking 비동기 처리에 적합

# BlockIO
# 순차 실행

import timeit
from urllib.request import urlopen

urls = ['http://daum.net', 'https://google.com', 'https://apple.com',
        'https://tistory.com', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()

# 순차 실행부
for url in urls:
    print('Start', url)
    # 실제 요청
    text = urlopen(url)
    # 실제 내용
    # print('Contents', text.read())

    print('Done', url)


# 완료시간 - 시작시간
duration = timeit.default_timer() - start

# 총 실행 시간
print('Total Time', duration)
