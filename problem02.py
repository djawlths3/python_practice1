# 문제1. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

def isnumber(no):
    try:
        int(no)
        return int(no)
    except ValueError:
        print('정수가 아닙니다')
        exit(0)


number = input('수를 입력하세요: ')
number = isnumber(number)
if(number % 2 != 0):
    print('홀수')
    exit(0)
else:
    print('짝수')
    exit(0)
