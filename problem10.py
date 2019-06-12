# 문제1. 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
#     - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )


def isnumber(no):
    try:
        int(no)
        if(int(no) < 0):
            print('음수입니다. 양수를 입력하세요')
            exit(0)
        return int(no)
    except ValueError:
        print('정수가 아닙니다')
        exit(0)

number = input('숫자를 입력하세요: ')
number = isnumber(number)
device = number % 2
result = 0
for x in range(1, number + 1):
   if(x % 2 == device):
       print(x)
       result += x


print('결과값 : ', result)