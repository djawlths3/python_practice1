# 문제1. 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴: ')

price = {'오뎅' : 300, '순대': 400, '만두': 500}
try:
    print('가격: ', price[menu])
except KeyError:
    print('가격: 0')

