# Asyncio
# 비동기 I/O Coroutine 작업(동기는 기다려야 한다. 비동기는 기다리지 않고 바로 실행. 다음 제어권을 넘겨 다음 워커가 일할 수 있게 해준다.)
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점 부터 재실행하는 원리
# Non-Blocking 비동기 처리에 적합

# BlockIO -> Thread 사용
# 쓰레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결

# aiohttp 사용 가능(Asyncio 지원)
from multiprocessing.pool import ThreadPool
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio

urls = ['http://daum.net', 'https://google.com', 'https://apple.com',
        'https://tistory.com', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()


async def fetch(url, executor):
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)
    return res.read()[0:5]


async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # asyncio.enure_future
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 생성
    loop = asyncio.get_event_loop()
    # 루프 대기
    loop.run_until_complete(main())
    # 함수 실행
    main()

    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total Time', duration)
