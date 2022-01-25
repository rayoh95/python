# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect("./resource/database.db")    # 본인 db 경로


# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
#print('One -> \n', c.fetchone())

# 지정 로우 선택
#print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
#print('All -> \n', c.fetchall())

#print('All -> \n', c.fetchall())

print()

# 순회1
rows = c.fetchall()
#for row in rows:
#    print('retrieve1 > ', row)


# 순회2
#for row in c.fetchall():
#    print('retrieve2 > ', row)


# 순회3
#for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#    print('retrieve3 > ', row)

print()


# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1) # ? 는 맵핑인 것을 잊지 말자
print('param1', c.fetchone())
print('param1', c.fetchall())   #데이터 없슴


# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall())   #데이터 없슴


# WHERE Retrieve3
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param2', c.fetchone())
print('param2', c.fetchall())   #데이터 없슴


# WHERE Retrieve4
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4',c.fetchall())


# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3,4))
print('param5',c.fetchall())


# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{"id1": 2, "id2": 5})
print('param6',c.fetchall())


# Dump 출력 - 서버, 혹은 컴퓨터가 바뀔 시 데이터베이스를 가져오는 작업
with conn:
    with open('./resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close() 호출이 with문 덕분에 호출이 자동으로 됐다.