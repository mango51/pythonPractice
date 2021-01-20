i,k,guguline = 0,0,''

for i in range(9,1,-1):
    guguline = guguline + (' #  %d단   # ' %i)

print(guguline)

for i in range(9,0,-1):
    guguline ='' #문자열 담는 변수 초기화, 위에서 사용해서 값 남아있음
    for k in range(9,1,-1):
        guguline = guguline + str('%2d X %2d = %2d'%(k,i,k*i))

    print(guguline) #한 행 출력하고 다음 포문으로 넘어갈 때는 초기화됨
