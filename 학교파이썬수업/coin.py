num = int(input('교환할 돈은 얼마? '))
print('500원 : ', num//500, '개')
left = num%500
print('100원 : ', left//100, '개')
left = left%100
print('50원 : ', left//50, '개')
left = left%50
print('10원 : ', left//10, '개')
left = left%10
print('바꾸지 못한 돈 : ', left, '원')

s1 = '123.1'
print(float(s1))

s2 = '123'
print(float(s2))
