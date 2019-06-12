# 문제1. 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.

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

won = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
number = input('수를 입력하세요: ')
number = isnumber(number)

for x in won:
    cnt, number = divmod(number, x)
    print(x,'원 : ',cnt,'개')