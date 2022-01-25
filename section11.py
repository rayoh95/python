# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv 

import csv

with open('./resource.sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)    # colum 명을 스킵한다(Header 스킵한다)

    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)
    



with open('./resource.sample1.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|')

    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)
    

# Dict 변환

with open('./resource.sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k,v)
        print('----------------------------')


# 예제4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]

with open('.resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


# 예제5
with open('.resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

