a = ord('A')
# ord()함수 = 문자를 ASCII코드 값으로 반환하는 함수
# 문자 A의 ASCII코드 값은 65
mask = 0x0F
#mask값 설정

print('%x & %x = %x' %(a,mask,a&mask))
# a= 65를 16진수= 0x41 = 0100 0001 (2진수)
# mask = 0000 1111 (2진수) = 0x0F (16진수)
# a & mask = 0000 0001 = 1 (10진수) = 1 (16진수)
# %x니까 16진수로 출력하기

print('%X & %X = %X' %(a,mask,a|mask))
# a = 65로 0100 0001 (2진수)
# mask = 0000 1111 (2진수)
# a|mask = 0100 1111 = 4F (16진수) >> 3번째 %X에 4F 출력하기
# %x니까 16진수로 출력하기

mask = ord('a') - ord('A')
#mask = 97 - 65 = 32

b = a^mask
# b = 65 ^ 32 (^는 비트 연산자이니 정수를 2진수로 변환하고 각 비트끼리 연산하기)
print('%c^%d=%c'%(a,mask,b))
# 연산결과 b = 97 이기에 a=65(A), mask = 32, b=97(a)
# %c로 되어있는 곳은 다 문자로 출력하기 (ASCII코드 값을 문자로 변환)
a = b^mask
# a = 97 ^ 32 = 65이기에 b= 97(a), mask =32, b=65 (A)
print('%c^%d=%c' %(b,mask,a))
# %c로 되어있는 곳은 다 문자로 출력하기 (ASCII코드 값을 문자로 변환)
