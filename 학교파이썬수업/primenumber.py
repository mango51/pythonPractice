num, isit = 0, True

num = int(input('숫자를 입력하세요 : '))

for i in range(2,num):
    if num %i ==0: #num미만의 숫자(2이상)에서 나누어 떨어졌을 때
        isit = False
        # 나누어지지 않으면 그대로 isit= True로 되어있음 (바뀌지 X)
        # 나누어질 때만 isit=False로 바뀜
        # if문 하나만 적었으니 (else 없음) 조건이 충족할 때만 실행문(isit=False) 성립됨
        
if isit == True: # 위에 있는 if문이 성립되지 않았을 때는 num은 소수임 (isit=True 그대로 남겨있음)
    print('%d는 소수입니다.' %num)
else: #isit = False일때... 소수가 아닐 때...
    print('%d는 소수가 아닙니다.' %num)
