print(0b10010011)

sel = int(input('진수 : '))

if sel != 10 and sel != 8 and sel != 16 and sel != 2:
    print('경고')
    exit();

num = input('값 입력 : ')

if sel == 16:
    num10 = int(num,sel)

if sel==10:
    num10 = int(num,sel)

if sel==8:
    num10 = int(num, sel)

if sel==2:
    num10=int(num,sel)

print('16진수 : ', hex(num10))
print('10진수 : ', num10)
print('8진수 : ', oct(num10))
print('2진수 : ', bin(num10))
