# 문제1. 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)

for x in range(1, 10):
    for y in range(1, 10):
        print(y, 'x', x , '=', y*x, end='\t')
        if (y == 9):
            print(end='\n')