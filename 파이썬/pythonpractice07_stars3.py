lines = int(input("줄 수를 입력해주세요 : "))

for i in range(lines):
    print(' '*(lines-i), end='')
    for j in range(0,i+1):
        print('*','',end='')
    print()

