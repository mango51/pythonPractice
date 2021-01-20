hap = 0
a,b = 0,0

while True:
    a = int(input('더할 첫 번째 수 : '))
    b = int(input('더할 두 번째 수 : '))
    hap = a+b
    print('%d + %d = %d' % (a,b,hap))
    # 무한 반복함 >> 출력한 뒤 다시 위로 올라가서 새롭게 a,b 값 받는다
