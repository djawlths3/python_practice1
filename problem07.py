# 문제1. 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

def isnumber(no):
    try:
        int(no)
        return int(no)
    except ValueError:
        print('정수가 아닙니다')
        exit(0)

number = []
for i in range(0,5):
    number.append(input('수를 입력하세요: '))
    number[i] = isnumber(number[i])

print('평균: ',sum(number,0.0)/len(number))