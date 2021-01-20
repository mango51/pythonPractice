import random

numbers=[] #빈 리스트인 numbers준비
for num in range(0,10):
    numbers.append(random.randrange(0,10))
    #1~9까지에서 랜덤으로 numbers리스트에 10가지 넣기

print(numbers)
#랜덤으로 10개의 값 넣은 numbers리스트

for num in range(0,10):
    if num not in numbers:
        print('%d 없음' %num)
        #numbers리스트에 없는 값은 없다고 출력하
