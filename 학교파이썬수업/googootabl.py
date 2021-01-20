i, k, guguline =0,0,''
#guguline은 문자열 저장하는 변수

for i in range(2,10):
    guguline = guguline + ('# %d단 # ' %i)

print(guguline)

for i in range(1,10): #외부 for문의 카운트변수
    guguline ='' #guguline 변수 초기
    for k in range(2,10): #내부 for문의 카운트변수
        guguline = guguline +str('%2dX%2d=%2d' %(k,i,i*k))
        #line 맞춰주기 위해서 2넣음 > 2칸으로 자리 마련

    print(guguline)

#구구단 테이블 한 행마다 출
