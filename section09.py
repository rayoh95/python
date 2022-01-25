# 파일 읽기, 쓰기
# 읽기 모드 : r , 쓰기 모드(기존 파일 삭제) : w , 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대경로

# 파일 읽기

f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print('--------------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))
    # with 문 안에서는 close 안해도 된다.

print('--------------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())


print('--------------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    conten = f.read()
    print(">", content)
    conten = f.read()
    print(">", content) # 빈 내용이 표시된다. 위에서 이미 한 번 읽었기 때문에. 


print('--------------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    print(line)
    while line:
        print(line, end=' #### ')
        line = f.readline()


print('--------------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end= ' ********* ')
    


print('--------------------------------------------------')

score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기

with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!')



with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')


from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')


# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Choi\n']
    f.writelines(list)


with open('./resource/text4.txt', 'w') as f:
    print('Test Contests1!', file=f)
    print('Test Contests21', file=f)


