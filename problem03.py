# 문제1. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.

for x in range(0, 10):
    for y in range(0, x):
        print('*', end='')
    print('')