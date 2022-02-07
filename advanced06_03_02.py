# Future 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> Network I/O 관련 작업 동시성 활용 권장
# 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상

# 실습 대상 3가지 경우

# 순차 실행
# concurrent.futuers 방법1
# concurrent.futuers 방법2

# Google Python GIL(Global Interpreter Lock)
# Gil 은 한 번에 하나의 스레드만 수행 할 수 있게 인터프리터 자체에서 락을 거는 것.(안전하기 때문에)

import os
import time
import sys
import csv
from concurrent import futures

# concurrent.future 방법1(ThreadPoolExecutor, ProcessPoolExecutor)
# map()
# 서로 다른 스레드 또는 프로세스에서 실행 가능
# 내부 과정을 알 필요 없으며, 고수준으로 인터페이스 제공


# 국가 정보
NATION_LS = (
    'Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()

# 초기 CSV 위치
TARGET_CSV = '/Users/oseunghwan/Desktop/Python/resources/nations.csv'

# 저장 폴더 위치
DEST_DIR = '/Users/oseunghwan/Desktop/Python/csvs'

# CSV 의 헤더정보
HEADER = ['Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority,', 'Order Date', 'Order ID',
          'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cose', 'Total Revenue', 'Total Cost', 'Total Profit']


# 국가 별 csv 파일 저장
def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, 'w', newline=' ') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerrow(row)


# 국가 별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict 을 list 로 적재
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # OrderedDict 확인
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data


# 중간 상황 출력
def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 지우기)
    sys.stdout.flush()


# 국가 별 분리 함수 실행
def separate_many(nt):
    # 분리 데이터
    data = get_sales_data(nt)
    # 상황 출력
    show(nt)
    # 파일 저장
    save_csv(data, nt.lower() + '.csv')

    return nt


# 시간 측정 및 메인함수
def main(seperate_many):
    # worker 개수
    worker = min(20, len(NATION_LS))    # 20 또는 NATION_LS 리스트의 크기 중 작은 수를 대입
    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    # ProcessPoolExecutor : GIL 우회, 변경 후 -> 내부적으로 os.cpu_count() 호출해서 cpu core 개수를 알아서 가져와 내부적으로 실행
    # ThreadPoolExecutor : GIL 종속, Thread 에 맞춰서 공통적으로 일어나는 I/O 작업을 분리하는게 좋다.
    # with futures.ThreadPoolExecutor(worker) as excutor:
    with futures.ProcessPoolExecutor() as excutor:
        # map -> 작업 순서를 유지하고 즉시 실행.
        result_cnt = excutor.map(separate_many, sorted(NATION_LS))
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = '\n{} csv separated in {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result_cnt), end_tm))


# 실행
if __name__ == '__main__':
    main(separate_many)
