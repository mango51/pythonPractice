a = 100
# a = 1100100 (2진수)
result = 0
i = 0

for i in range(1,5):
    result = a <<i
    # i가 1일때, result = 1100100 << 1 = 11001000 = 200 = 100*2
    # i가 2일때, result = 1100100 << 2 = 110010000 = 16+128+256 = 400 = 100*2의 2승
    print('%d << %d = %d' % (a,i,result))
    # i가 1일때, a=100, i=1, result =200
    # i가 2일때, a=100, i=2, result=400
    # a=100은 전역변수로 지정되어있음 >> 반복문이 돌아갈 때 전역변수 a=100 가져옴

for i in range(1,5):
    result = a>>i
    print('%d >> %d = %d' % (a,i,result))
