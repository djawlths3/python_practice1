# 문제1. 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.




str = input('문자를 입력하세요: ')
for i in range(len(str)-1, -1, -1):
    print(str[i], end='')