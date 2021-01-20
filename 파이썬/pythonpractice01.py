num = int(input('1000이하의 자연수를 입력하세요 : '))

total = 0
total2 = 0

if num >= 1000:
    print('1000 자연수를 입력하세요')
else:
    num3 = int(num/3)
    for i in range(num3+1):
        total += i*3
    num5 = int(num/5)
    for i in range(num5+1):
        total2 += i*5

print(num,'이하의 자연수 중 3의 배수의 합 : ', total)
print(num,'이하의 자연수 중 5의 배수의 합 : ',total2)
