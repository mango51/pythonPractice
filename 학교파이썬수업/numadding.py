num1,num2,num3,answer =0,0,0,0

num1 = int(input('첫 번째 숫자? '))
num2 = int(input('두 번째 숫자? '))
num3 = int(input('더할 숫자? '))

for i in range(num1,num2+1,num3):
    answer += i
print('%d +%d +...+%d는 %d입니다.'%(num1,num1+num3,num2,answer))
